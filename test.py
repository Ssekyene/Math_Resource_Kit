from models import storage
from models.concept import Concept
from models.resource import Resource
from models.activity import Activity
from models.quiz import Quiz
from models.option import Option
import random

# concepts = ['Number Bases', 'Working with Integers', 'Fractions, Percentages and Decimals', 'Rectangular Cartesian Coordinates in 2-Dimensions', 'Geometric Construction Skills', 'Sequence and patterns', 'Bearings', 'General and angle properties of geometric figures', 'Data collection and presentation', 'Reflection', 'Equation of lines and Curves', 'Algebra 1', 'Business arithmetics', 'Time and time tables']

# clen = len(concepts)
# for i in range(0, clen):
#     numbers = Concept(name=concepts[i], priority=i+1, introduction="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Multoque hoc melius nos veriusque quam Stoici. Quoniam, si dis placet, ab Epicuro loqui discimus. Respondent extrema primis, media utrisque, omnia omnibus. Haec para/doca illi, nos admirabilia dicamus. Cum autem in quo sapienter dicimus, id a primo rectissime dicitur. Duo Reges: constructio interrete. Et ille ridens: Video, inquit, quid agas; Ergo adhuc, quantum equidem intellego, causa non videtur fuisse mutandi nominis.", conclusion="Equidem, sed audistine modo de Carneade? Quis enim redargueret? Dulce amarum, leve asperum, prope longe, stare movere, quadratum rotundum. Collige omnia, quae soletis: Praesidium amicorum. At eum nihili facit; Etenim semper illud extra est, quod arte comprehenditur. Inscite autem medicinae et")
#     print(numbers)
#     numbers.save()



# concept_objs = storage.all(Concept).values()
# for val in concept_objs:
#     print(val)

# objs = storage.all()
# for val in objs.values():
#     print(val)

# d_list = ["Lorem ipsum dolor sit amet", "Cum ageremus, inquit, vitae", "Cum ageremus, inquit, vitae", "Lorem ipsum dolor sit amet", "voluptatem vocant. Ad eas enim res", "voluptatem vocant.res", "Si id dicis, vicimus", "Lorem ipsum dolor sit amet", "Cum ageremus", "Si id dicis, vicimus"]
# u_list = ["Lorem ipsum dolor sit amet", "Cum ageremus, inquit, vitae", "Cum ageremus, inquit, vitae", "Lorem ipsum dolor sit amet", "voluptatem vocant. Ad eas enim res", "voluptatem vocant.res", "Si id dicis, vicimus", "Lorem ipsum dolor sit amet", "Cum ageremus", "Si id dicis, vicimus"]

# listlen = len(d_list)
# for i in range(0, listlen):
#     res = Resource(description=d_list[i], url=u_list[i])
#     print(res)
#     res.save()

# res_list = ["6857f84a-f709-45be-8b9c-3d4e9201617c", "da825687-231e-41c7-a26d-967beae1e760", "7dc55fae-33f3-4c1e-8177-99285399cbdb", "672df3fc-b576-4b0c-93ac-7c01ce750f53", "45d85396-3687-4264-a9e6-dfbe67355aa5", "fac32698-d5b1-4571-8b3d-728deb4f1852", "5a64b37a-8d7e-4c35-8f58-bd9ae2b5bb20", "0c07dd48-497b-45e5-a917-5f0f35592448", "4351a53a-9857-492b-804e-63cb3bdd9d7e", "da6588dc-d077-4ba4-8b4b-4cab4b4afaeb"]

# res_objs = list(storage.all(Resource).values())
# rlen = len(res_objs)
# concept_list = ["1c536e64-c053-4d00-923f-df75db1cc470", "21457c15-3b21-4fd1-aa2a-acb7d70cb39b", "23d065cc-1531-41fc-ae14-f773f7764fd7", "5bc3de84-f34b-412d-9b54-227878c59b58", "643fa853-c51c-44cd-a28e-3618ebc71107", "7c254b2c-2d90-4f99-8c62-d3460bab36cf", "7c7afba5-31f2-4a30-925b-99b390aed07c", "819ec6e8-373a-41c9-a204-183fc29338e1", "87d832ca-8ff6-4b2f-9280-62ab000d2352", "8d2ea209-a7ce-4582-9383-4f1bad6977a8", "924fd130-7495-4934-b09c-b4ef5b065dc8", "b5d17843-3754-4fb5-a6f9-78dc12779e05", "bff7a155-5194-46bf-b0ca-8a2a195f496b", "c22bd056-fb3b-4688-818f-8267529a80b0"]
# for id in concept_list:
#     concept = storage.get(Concept, id)
#     print(concept)
#     rnum = random.randint(1, rlen)
#     for i in range(0, rnum):
#         concept.resources.append(res_objs[i])
#     concept.save()

# concepts = storage.all(Concept).values()
# for c in concepts:
#     print(f" Concept: {c.name}\nResources:")
#     for r in c.resources:
#         print(f"\t->{r.id}")
#     print()

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
# desc_list = ["Laut cogitari esse aliquod animal, quod se oderit? Quid censes in Latino fore?", "Nunc dicam de voluptate, nihil scilicet novi, ea tamen, quae te?", "Itaque hic ipse iam pridem est reiectus..."]
# cor_opt_list = ["A", "B", "C", "D"]
# def create_quiz(cpt):
#     quiz_l = []
#     for desc in desc_list:
#         c_opt = random.choice(cor_opt_list)
#         quiz = Quiz(description=desc, correct_option=c_opt, concept=cpt)
#         print(quiz)
#         quiz_l.append(quiz)
#     return quiz_l

# opt_desc_l = ["illa autem voluptas ipsius", "illa autem voluptas ipsius in motu est", "illa autem voluptas", "illa autem voluptas ipsius"]

# for cpt in concept_objs:
#     quiz_l = create_quiz(cpt)
#     for quiz in quiz_l:
#         opt_l = []
#         for desc in opt_desc_l:
#             ident = random.choice(cor_opt_list)
#             opt = Option(description=desc, identifier=ident)
#             print(opt)
#             opt_l.append(opt)
#         quiz.options.extend(opt_l)
#         for opt in opt_l:
#             opt.save()
#     cpt.save()
#     for cq in quiz_l:
#         cq.save()


# act = storage.get(Activity, "72864aa6-cc9d-484f-b9c6-4ca2d3954b15")
# print(act)


# quizzes = storage.all(Quiz).values()
# c = 0
# for quiz in quizzes:
#     quiz.delete()
#     c += 1
#     if c == 10:
#         break
# storage.save()