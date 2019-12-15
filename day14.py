# day14
import pprint

formula = \
    """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

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
        if self.stock.get(ingre_chemical, 0) >= required_chems:
            self.stock.setdefault(ingre_chemical, 0)
            self.stock[ingre_chemical] -= required_chems
        else:
            self.make(ingre_chemical)
            self.stock[ingre_chemical] -= required_chems
            

    def make(self, chemical):
        print(f"required: {self.reactions[chemical]['ingredients']}")
        if "ORE" in self.reactions[chemical]['ingredients'].keys():
            self.used_ore += self.reactions[chemical]['ingredients']['ORE']
        else:
            for ingre_chemical in self.reactions[chemical]['ingredients']:
                required_chems = self.reactions[chemical]['ingredients'][ingre_chemical]
                self.get_from_stock_or_create(ingre_chemical, required_chems)

        self.stock[chemical] = self.reactions[chemical]['count']

    def collect_ingred(self, chemical):
        print(f"collecting reqs for {chemical}")
        if "ORE" in self.reactions[chemical]['ingredients'].keys():
            self.used_ore += self.reactions[chemical]['ingredients']['ORE']
        else:
            for chemical in self.reactions[chemical]['ingredients']:
                used_ore += collect_ingred(chemical, reactions)


factory = Chemical_factory()

factory.parse_reactions(formula)

pprint.pprint(factory.reactions)

factory.make("FUEL")

print(f"Used ore {factory.used_ore}")
print(f"Stock left {factory.stock}")
