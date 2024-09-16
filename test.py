from models import storage
from models.concept import Concept
from models.resource import Resource
from models.activity import Activity
from models.quiz import Quiz
from models.option import Option

# concepts = ['Number Bases', 'Working with Integers', 'Fractions, Percentages and Decimals', 'Rectangular Cartesian Coordinates in 2-Dimensions', 'Geometric Construction Skills', 'Sequence and patterns', 'Bearings', 'General and angle properties of geometric figures', 'Data collection and presentation', 'Reflection', 'Equation of lines and Curves', 'Algebra 1', 'Business arithmetics', 'Time and time tables']

# clen = len(concepts)
# for i in range(0, clen):
#     numbers = Concept(name=concepts[i], priority=i+1, introduction="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Multoque hoc melius nos veriusque quam Stoici. Quoniam, si dis placet, ab Epicuro loqui discimus. Respondent extrema primis, media utrisque, omnia omnibus. Haec para/doca illi, nos admirabilia dicamus. Cum autem in quo sapienter dicimus, id a primo rectissime dicitur. Duo Reges: constructio interrete. Et ille ridens: Video, inquit, quid agas; Ergo adhuc, quantum equidem intellego, causa non videtur fuisse mutandi nominis.", conclusion="Equidem, sed audistine modo de Carneade? Quis enim redargueret? Dulce amarum, leve asperum, prope longe, stare movere, quadratum rotundum. Collige omnia, quae soletis: Praesidium amicorum. At eum nihili facit; Etenim semper illud extra est, quod arte comprehenditur. Inscite autem medicinae et")
#     print(numbers)
#     numbers.save()



# concept_obj = storage.all(Concept)
# for val in concept_obj.values():
#     obj_dict = val.to_dict()
#     for val in obj_dict.values():
#         print(val)
# objs = storage.all()
# for val in objs.values():
#     print(val)

# res = Resource(description="Duo Reges: constructio", url="Non est igitur summum malum dolor")
# print(res)
# concept = storage.get(Concept, "22e9f662-31eb-4435-8b90-8a006a5669ad")
# print(concept)
# concept.resources.append(res)
# res.save()
# concept.save()

# concept = storage.get(Concept, "22e9f662-31eb-4435-8b90-8a006a5669ad")
# print(concept)
# for res in concept.resources:
#     print(res)
# activity = Activity(description="His singulis copiose responderi solet, sed quae perspicua sunt longa esse non debent. Quid ergo hoc loco intellegit honestum? Hoc non est positum in nostra actione.", concept=concept)
# print(activity)
# activity.save()

# concept = storage.get(Concept, "22e9f662-31eb-4435-8b90-8a006a5669ad")
# print(concept)
# quiz = Quiz(description="laut cogitari esse aliquod animal, quod se oderit? Quid censes in Latino fore?", correct_option="A", concept=concept)
# print(quiz)
# quiz.save()

# numbers = Concept(name="Numbers", introduction="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Multoque hoc melius nos veriusque quam Stoici. Quoniam, si dis placet, ab Epicuro loqui discimus. Respondent extrema primis, media utrisque, omnia omnibus. Haec para/doca illi, nos admirabilia dicamus. Cum autem in quo sapienter dicimus, id a primo rectissime dicitur. Duo Reges: constructio interrete. Et ille ridens: Video, inquit, quid agas; Ergo adhuc, quantum equidem intellego, causa non videtur fuisse mutandi nominis.", conclusion="Equidem, sed audistine modo de Carneade? Quis enim redargueret? Dulce amarum, leve asperum, prope longe, stare movere, quadratum rotundum. Collige omnia, quae soletis: Praesidium amicorum. At eum nihili facit; Etenim semper illud extra est, quod arte comprehenditur. Inscite autem medicinae et")
# print(numbers)
# numbers.save()

# concept_obj = storage.all(Concept)
# for val in concept_obj.values():
#     obj_dict = val.to_dict()
#     for val in obj_dict.values():
#         print(val)
# objs = storage.all()
# for val in objs.values():
#     print(val)

# res = Resource(description="Duo Reges: constructio", url="Non est igitur summum malum dolor")
# print(res)
# concept = storage.get(Concept, "22e9f662-31eb-4435-8b90-8a006a5669ad")
# print(concept)
# concept.resources.append(res)
# res.save()
# concept.save()

# concept = storage.get(Concept, "22e9f662-31eb-4435-8b90-8a006a5669ad")
# print(concept)
# activity = Activity(description="His singulis copiose responderi solet, sed quae perspicua sunt longa esse non debent. Quid ergo hoc loco intellegit honestum? Hoc non est positum in nostra actione.", concept=concept)
# print(activity)
# activity.save()

# concept = storage.get(Concept, "22e9f662-31eb-4435-8b90-8a006a5669ad")
# print(concept)
# quiz = Quiz(description="laut cogitari esse aliquod animal, quod se oderit? Quid censes in Latino fore?", correct_option="A", concept=concept)
# print(quiz)
# quiz.save()

# quiz = storage.get(Quiz, "55a11d7a-4eb6-44af-92ab-542a998567d3")
# print(quiz)
# option1 = Option(description="illa autem voluptas ipsius")
# option2 = Option(description="illa autem voluptas ipsius in motu est")
# option3 = Option(description="illa autem voluptas")
# option4 = Option(description="illa autem voluptas ipsius disputationem volo, nec tua mihi oratio")
# options = [option1, option2, option3, option4]
# for opt in options:
#     print(opt)
# quiz.options.extend([option1, option2, option3, option4])
# for opt in options:
#     opt.save()
# quiz.save()

# act = storage.get(Activity, "72864aa6-cc9d-484f-b9c6-4ca2d3954b15")
# print(act)