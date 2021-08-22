from kanji_list import kanji_list


def main():
    # 漢字一覧インスタンスを作成
    kl = kanji_list.KanjiList()

    # 常用漢字の一覧を取得
    kl.get_jyoyo_kanji_list()

    # 人名用漢字の一覧を取得
    kl.get_jinmei_kanji_list()

    # 常用漢字と人名用漢字の一覧を結合
    kl.join_kanji_list()

    # 漢字一覧をtsvとして取得
    kl.output_kanji_list()

if __name__=='__main__':
    main()
