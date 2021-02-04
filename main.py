# This is a sample Python script.
import MeCab
from wordcloud import WordCloud


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def make_wordcloud():
    # Use a breakpoint in the code line below to debug your script.
    f = open('kokoro2.txt', 'r', encoding='utf-8')
    text = f.read()
    f.close()

    m = MeCab.Tagger('-Ochasen')

    word = "word word word text school ok hoge 田中"
    node = m.parseToNode(text)
    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi in ["名詞", "形容詞", "動詞"]:
            origin = node.feature.split(",")[6]
            word = word + " " + origin
        node = node.next
    fon_path = r"C:\Windows\Fonts\YuGothB.ttc"
    wordcloud = WordCloud(background_color="white", font_path=fon_path, width=600, height=400, min_font_size=15)
    wordcloud.generate(word)

    wordcloud.to_file("wordcloud.png")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_wordcloud()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
