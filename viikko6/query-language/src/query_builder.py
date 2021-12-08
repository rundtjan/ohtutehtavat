from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

class QueryBuilder:
    def __init__(self, matcher = All):
        self.matcher_olio = matcher

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.matcher_olio))

    def hasAtLeast(self, *args):
        return QueryBuilder(And(HasAtLeast(args[0], args[1]), self.matcher_olio))

    def hasFewerThan(self, *args):
        return QueryBuilder(And(HasFewerThan(args[0], args[1]), self.matcher_olio))
    
    def OneOf(self, matcher_one, matcher_two):
        return Or(matcher_one, matcher_two)

    def build(self):
        return self.matcher_olio