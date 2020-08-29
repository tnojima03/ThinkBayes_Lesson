from thinkbayes import Pmf

#まずは全体像を見る。下の方に各メソッドごとの説明を載せておく。
class Cookie(Pmf):  # 引数に仮説の配列を取る
    def __init__(self, hypos):  # 事前確率 P(H) の設定。
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)  # selfはクラス自身なので、self.Set()はCookie.Set()のこと
        self.Normalize()

    mixes = {
        'Bowl1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl2': dict(vanilla=0.5, chocolate=0.5),
    }

    def Likelihood(self, data, hypo):  # 尤度 P(D|H) の設定。各仮説の下でのデータが得られる確率。
        mix = self.mixes[hypo]
        like = mix[data]  # like = P(D|H)
        return like

    def Update(self, data):  # 事後確率 P(H|D) の計算。
        for hypo in self.Values():  # ここで、self.Valuesは仮説の配列を返す。
            like = self.Likelihood(data, hypo)  # Cookie.Likelihood()のこと。自身のクラスのメソッドを呼んでいる。
            self.Mult(hypo, like)
        self.Normalize()  # 規格化

#実際の計算
hypos = ['Bowl1', 'Bowl2']   #仮説の配列を設定
pmf = Cookie(hypos)          #インスタンス作成

pmf.Values()     #ちなみに、pmf.Values()は仮説の配列を返す。
                 #出力すると  dict_keys(['Bowl1', 'Bowl2'])  が得られる。
pmf.Items()      #ベイズ更新前の各仮説の成立確立を見てみると、これは事前確率なので両方0.5
                 #出力すると、 dict_items([('Bowl1', 0.5), ('Bowl2', 0.5)])　が得られる。

pmf.Update('vanilla')     # vanillaが出たというデータを用いてベイズ更新
pmf.Items()     #ベイズ更新後の各仮説の生起確率を見てみると、値が更新されていることが分かる 。
                #出力すると、 dict_items([('Bowl1', 0.6000000000000001), ('Bowl2', 0.4)])  が得られる。

"""
(注) self.nameはクラスで定義された値や辞書を返す。self.func()はクラスで定義された関数を呼び出す。()のある無しを
　　 注意深く観察すると良い。
"""



"""上記のクラスについて、各メソッドの説明を書いておく。"""

#p13 clsss Cookieについて
class Cookie(Pmf):
    def __init__(self, hypos):      #初期化メソッドでhypos(仮説)の一覧の設定。引数は仮説。
        Pmf.__init__(self)
        for hypo in hypos:         #仮説の一覧から一つずつ仮説を取り出し、全て事前確率を１にセット。この場合一様分布。
            self.Set(hypo, 1)
        self.Normalize()          #規格化して各仮説の生起確率の和を１にする。

#p14 Updateメソッドは、新しいデータをもとにPMF（確率質量関数）を更新するメソッド。引数はデータ。
# Updates the PMF with new data.   data: string cookie type
def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()


# 　mixesは、各ボウルの中の各クッキーが取り出される確率を格納したディクショナリ
mixes = {
    'Bowl1': dict(vanilla=0.75, chocolate=0.25),
    'Bowl2': dict(vanilla=0.5, chocolate=0.5),
}


# 　Likelihoodは、尤度を計算するメソッド。引数はデータと仮説。
def Likelihood(self, data, hypo):
    """The likelihood of the data under the hypothesis.
    data: string cookie type
    hypo: string bowl ID
    """
    mix = self.mixes[hypo]  # mixes(辞書型)から仮説名（この場合はBowl1 または 2）をキーとしてそれに対応する辞書を得る.
    # 例えば仮説がBowl1なら、mixは{'vanilla':0.75, 'chocolate':0.25}という辞書。
    like = mix[data]  # 辞書mixからデータが得られる確率を取り出す。
    return like

