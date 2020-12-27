"""
Şirket Otomosyonu
Eren Özatak
27.12.2020
"""

class Sirket():

    def __init__(self,sirketİsmi,mudurler, mudurYrdm,calısanSayısı,faliyetDurumu):
        self.sirketİsmi=sirketİsmi
        self.mudurler=mudurler
        self.mudurYrdm=mudurYrdm
        self.calısanSayısı=calısanSayısı
        self.faliyerDurumu=faliyetDurumu

    def bilgiler(self):
        print(f"""
             
              {self.sirketİsmi }
     *//**//*/**//*/*/**//**//**//**/*/*/*//**//*
        Müdürler: {self.mudurler }
        Müdür Yardımcıları: {self.mudurYrdm }
        Çalışan sayısı: {self.calısanSayısı }
        Faliyet Durumu: {self.faliyerDurumu }

     *//**//*/**//*/*/**//**//**//**/*/*/*//**//*
        """)

Seheren = Sirket("Seheren Holding", ["Seher","Eren"] ,["Sevgi Güngör","Umut Günebakan","Mariya Er","Beren Yiğit"], 280, True)

Seheren.bilgiler()















