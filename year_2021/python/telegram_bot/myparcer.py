from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json
import datetime
import re

from pmdarima.arima import auto_arima


def get_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    page = BeautifulSoup(driver.page_source, 'lxml')
    driver.quit()
    return page


def get_name(page):
    """
    Возвращает название манги
    """
    return page.find('div', class_='media-name__main').text.strip()


def get_status(page):
    """
    Возвращает статус манги: анонс, онгоинг, завершен, приостановлен
    """
    index = list(map(lambda x: x.text.strip(), page.find_all('div', class_='media-info-list__title'))).index('Статус тайтла')
    return page.find_all('div', class_='media-info-list__value')[index].text.strip()


def get_latest_date(page):
    """
    Возвращает дату последней публикации перевода
    """
    return page.find_all('div', 'media-chapter__date')[0].text.strip()


def get_latest_chapter_name(page):
    """
    Возвращает название последней главы
    """
    return page.find_all('div', class_='media-chapter__name text-truncate')[0].text.strip()


def add_manga(url, manga_list):
    """
    Добавляет мангу в список "избранного" (manga_list):
    по тайтлам из этого списка будут присылаться уведомления на обновления
    """
    if re.compile('^https://mangalib.me.').match(url):
        page = get_page(url)

        if get_status(page) != 'Онгоинг':
            return 'Манга завершена/заморожена. Новых глав в ближайшем будущем не будет 😭'

        try:
            get_latest_date(page)

            name = get_name(page)

            manga_list['url'][name] = url
            manga_list['name'][name] = name
            manga_list['status'][name] = get_status(page)
            manga_list['latest_date'][name] = get_latest_date(page)
            manga_list['latest_chapter_name'][name] = get_latest_chapter_name(page)

            return 'Манга добавлена в избранное. Если хотите добавить еще, нажмите /add'

        except:
            return 'Перевода нет в открытом доступе'

    else:
        return 'Неверный формат ссылки'


def favorites(manga_list):
    """
    Возвращает список избранных тайтлов
    """
    return list(manga_list['url'].keys())


def delete_manga(name, manga_list):
    """
    Удаляет мангу из списка избранных
    """
    if name in manga_list['url'].keys():
        for key in manga_list.keys():
            del manga_list[key][name]
        return 'Манга удалена из избранного'

    else:
        return 'Данный тайтл не в избранном'


def check_new_chapter(name, manga_list):
    """
    Проверяет, вышла ли новая глава манги
    Возвращает True, если вышла, иначе - False; обновляет список "избранного"
    """
    page = get_page(manga_list['url'][name])

    if get_latest_chapter_name(page) != manga_list['latest_chapter_name'][name]:
        manga_list['latest_chapter_name'][name] = get_latest_chapter_name(page)
        manga_list['latest_date'][name] = get_latest_date(page)
        return True
    else:
        return False


def new_chapters_list(manga_list):
    """
    Возвращает список тайтлов из "избранного" (manga_list), для которых вышла новая глава
    """
    return [name for name in manga_list['url'].keys() if check_new_chapter(name, manga_list) is True]


def predict(name, manga_list):
    """
    Делает прогноз на дату выхода следующей главы
    """
    if name in manga_list['url'].keys():
        page = get_page(manga_list['url'][name])

        dates = list(map(lambda x: datetime.datetime.strptime(x.text.strip(), '%d.%m.%Y'),
                         page.find_all('div', class_='media-chapter__date')))
        dates.sort()
        dates = dates[-10:]
        if len(dates) <=2:
            return 'Нельзя сделать прогноз'
        else:
            intervals = [(dates[i] - dates[i - 1]).days for i in range(1, len(dates))]
            model = auto_arima(intervals)
            pred_date = dates[-1] + datetime.timedelta(model.predict(1)[0] // 1 + 1)
            return pred_date.strftime('%d.%m.%Y') if pred_date > datetime.datetime.today() else 'Нельзя сделать прогноз'

    else:
        return 'Данный тайтл не в избранном'


def save_json(file_name: str, manga_list: dict):
    with open(file_name + '.json', 'w') as fp:
        json.dump(manga_list, fp)


def load_json(file_name: str):
    with open(file_name + '.json', 'r') as fp:
        manga_list = json.load(fp)
    return manga_list
