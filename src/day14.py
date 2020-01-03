# day14
import pprint

formula = \
    """2 JNLZG => 7 SJTKF
1 BDCJZ, 3 NWCRL => 5 PMQS
1 TNRBS => 2 LHNGR
7 TWHBV => 6 FLQSP
4 DNLQF, 3 DRFL, 4 RSHRF => 6 HXJFS
5 VHSLS => 7 DZDQN
11 STPXT, 16 XRTW => 1 CTZFK
5 BXWD => 2 RVNR
1 XRTW, 2 SJTKF => 2 FPKWZ
1 JMGDP, 3 TJLKW => 7 FNLF
26 DTQTB, 16 TWHBV => 3 JMGDP
1 DFRNL, 1 LHNGR => 9 NWCRL
2 NWPC, 2 LHNGR, 3 QCHC => 8 HPBP
10 CSKJQ => 4 QRSD
8 FVLQ => 6 WMBVF
11 NPVB, 12 QRFV => 6 STPXT
3 SJTKF, 1 NPVB => 7 GWHG
4 DKPKX, 1 SJPWK => 5 DTQTB
1 RVNR => 8 XRTW
67 KGVR, 1 ZLJR, 4 TBPB, 19 KPJZM, 8 QSWQ, 12 DTQTB, 15 QRSD, 4 FPKWZ => 1 FUEL
20 LHNGR, 6 DNLQF, 9 TWHBV => 8 SJPWK
1 QRSD, 11 HZWS => 5 KGVR
2 CTZFK, 1 DRFL, 1 TNRBS => 5 DKPKX
14 FVFTN, 2 VLKQ, 12 STPXT => 4 TWHBV
1 FXWRB, 1 BXWD => 8 FVFTN
12 NPVB, 2 KJWC, 1 JNLZG => 3 NDNZP
13 NPVB, 7 HZLKM => 3 ZRMQC
2 HXJFS, 14 PDGB, 2 FNLF => 1 FVLQ
7 QRFV, 10 QRSD, 6 FVFTN => 5 DNLQF
4 XQDC, 2 VHSLS => 1 BDCJZ
9 HZLKM, 1 NDNZP => 6 DRFL
147 ORE => 4 BXWD
6 DNLQF => 5 VCBFZ
1 FVFTN => 8 TNRBS
1 RSHRF, 2 PDGB, 1 MKWH, 4 QRSD, 11 DNLQF, 7 WMBVF, 1 HJHM => 8 QSWQ
6 PMQS, 2 HNTS => 1 WNVGC
4 RVNR, 6 GWHG => 2 VLKQ
11 DRFL, 1 PDGB => 6 DFRNL
3 WNVGC, 28 PFZN, 14 HNTS, 2 WMBVF, 18 VCBFZ, 2 HPBP, 2 PDGB => 6 TBPB
2 XQDC => 6 HZWS
7 JNLZG, 1 BXWD, 7 FXWRB => 5 KJWC
9 KJWC, 7 NDNZP => 4 CSKJQ
194 ORE => 9 FXWRB
2 VHSLS, 12 MKWH, 2 FWBL, 6 TJLKW, 9 HZWS, 11 ZQGXM => 5 ZLJR
139 ORE => 2 JNLZG
2 TNRBS => 2 QCHC
7 DRFL, 10 STPXT, 1 QRSD => 6 MKWH
9 JNLZG => 8 NPVB
3 RSHRF => 6 FWBL
7 NDNZP => 5 PDGB
2 FVFTN => 6 QRFV
1 QRSD, 22 XQDC => 3 VHSLS
2 FVFTN => 3 HZLKM
6 ZRMQC => 2 PFZN
12 QRFV, 6 HZLKM => 6 XQDC
12 JMGDP, 1 KPJZM, 10 ZPKP => 5 HJHM
23 JNLZG => 2 ZQGXM
1 TJLKW => 9 HNTS
1 HZLKM, 12 PMQS => 5 KPJZM
7 DNLQF => 9 NWPC
1 FLQSP => 6 ZPKP
5 VLKQ => 7 RSHRF
6 TNRBS, 4 DZDQN, 6 TWHBV => 6 TJLKW"""

formula = formula.splitlines()

formula = [x.split("=>") for x in formula]


class Chemical_factory():
    stock = {}
    reactions = {}
    used_ore = 0

    def parse_reactions(self, formula):
        for chem in formula:
            chem_reaction = {}
            result = chem[1].split()
            result_chem = result[1]
            result_count = result[0]

            chem_reaction['count'] = int(result_count)

            ingredients = chem[0].split(",")
            chem_reaction['ingredients'] = {}
            for ing in ingredients:
                ing_lst = ing.split()
                chem_reaction['ingredients'][ing_lst[1]] = int(ing_lst[0])

            self.reactions[result_chem] = chem_reaction

    def get_from_stock_or_create(self, ingre_chemical, required_chems):
        
        self.stock.setdefault(ingre_chemical, 0)
        self.stock[ingre_chemical] -= required_chems
        while self.stock[ingre_chemical] < 0:
            self.make(ingre_chemical)

            
    def make(self, chemical):
        if "ORE" in self.reactions[chemical]['ingredients'].keys():
            self.used_ore += self.reactions[chemical]['ingredients']['ORE']
        else:
            for ingre_chemical in self.reactions[chemical]['ingredients']:
                required_chems = self.reactions[chemical]['ingredients'][ingre_chemical]
                self.get_from_stock_or_create(ingre_chemical, required_chems)
        self.stock.setdefault(chemical,0)
        self.stock[chemical] += self.reactions[chemical]['count']

    def collect_ingred(self, chemical):
        if "ORE" in self.reactions[chemical]['ingredients'].keys():
            self.used_ore += self.reactions[chemical]['ingredients']['ORE']
        else:
            for chemical in self.reactions[chemical]['ingredients']:
                used_ore += collect_ingred(chemical, reactions)


factory = Chemical_factory()
factory.parse_reactions(formula)

# pprint.pprint(factory.reactions)

###
### Part 1
###
# factory.make("FUEL")

# print(f"Used ore {factory.used_ore}")
# print(f"Stock left {factory.stock}")


#
# Part 2
#
factory.used_ore = -1000000000000

while factory.used_ore <=0:
    factory.make("FUEL")
    # print(factory.used_ore)
print(factory.stock['FUEL']-1) #dunno why -1, but is correct. Took 2h+ to compute

