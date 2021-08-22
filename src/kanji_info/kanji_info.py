from scraping import scraping_utils


class KanjiInfo:
    def __init__(self, kanji, url, type) -> None:
        self.kanji = kanji
        self.url = url
        self.type = type
    
    def get_yomi(self, soup):
        """漢字の読みを取得し、インスタンス変数に格納する

        Args:
            soup (BeautifulSoup): 漢字ページをパースしたBeautifulSoupオブジェクト
        """
        yomi_tag = soup.select('h2')[0].next_sibling.next_sibling

        # 音読み
        onyomi_tag_list = [tag for tag in yomi_tag.select('img')[1].previous_siblings]
        onyomi_list = [tag.get_text() for tag in onyomi_tag_list if 'span' in str(tag)]
        self.onyomi = onyomi_list

        # 訓読み
        kunyomi_tag_list = [tag for tag in yomi_tag.select('img')[1].next_siblings]
        kunyomi_list = [tag.get_text() for tag in kunyomi_tag_list if 'span' in str(tag)]
        self.kunyomi = kunyomi_list

        # 人名読み
        # TOOD後で実装する
    
    def get_imi(self, soup):
        """漢字の意味を取得し、インスタンス変数に格納する

        Args:
            soup (BeautifulSoup): 漢字ページをパースしたBeautifulSoupオブジェクト
        """
        imi_tag = soup.select_one('ul.imi')
        imi_tag.find('span', {'class': 'zigi2'}).extract()
        imi_list = [str(tag.get_text()) for tag in imi_tag.select('li')]
        self.imi = "\n".join(imi_list)

    def get_kakusu(self, soup):
        """漢字の画数を取得し、インスタンス変数に格納する

        Args:
            soup (BeautifulSoup): 漢字ページをパースしたBeautifulSoupオブジェクト
        """
        kakusu_tag = soup.select('h2')[3].next_sibling.next_sibling
        kakusu = kakusu_tag.get_text().replace('画', '')
        self.kakusu = int(kakusu)

    def main(self):
        soup = scraping_utils.get_soup_from_url(self.url)
        self.get_yomi(soup)
        self.get_imi(soup)
        self.get_kakusu(soup)

if __name__=='__main__':
    kanji = '丞'
    url = 'https://kanjitisiki.com/zinmei/002.html'
    type = '人名用'
    ki = KanjiInfo(kanji, url, type)
    ki.main()
    
    print(ki.onyomi)
    print(ki.kunyomi)
    print(ki.imi)
    print(ki.kakusu)
