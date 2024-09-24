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
# u_list = ["https://www.youtube.com/", "https://test.com/", "https://simple.wikipedia.org/wiki/Main_Page", "https://simple.wikipedia.org/wiki/Main_Page", "https://www.youtube.com/", "https://www.youtube.com/", "https://test.com/", "https://simple.wikipedia.org/wiki/Main_Page", "https://test.com/", "https://www.youtube.com/"]

# listlen = len(d_list)
# for i in range(0, listlen):
#     res = Resource(description=d_list[i], url=u_list[i])
#     print(res)
#     res.save()


# res_objs = list(storage.all(Resource).values())
# rlen = len(res_objs)

# for concept in concept_objs:
#     print(concept)
#     rnum = random.randint(1, rlen)
#     random.shuffle(res_objs)
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

# all_res = storage.all(Resource)
# for res in all_res.values():
#     res.delete()
# storage.save()

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
#         i = 0
#         for desc in opt_desc_l:
#             ident = cor_opt_list[i]
#             opt = Option(description=desc, identifier=ident)
#             print(opt)
#             opt_l.append(opt)
#             i += 1
#         quiz.options.extend(opt_l)
#         for opt in opt_l:
#             opt.save()
#     cpt.save()
#     for cq in quiz_l:
#         cq.save()

# a_desc = ["Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cum perferendis aut molestias? Quia consectetur, saepe veritatis excepturi quaerat porro sunt illo eaque eum expedita voluptatibus? <b>(answers: <i>Lorem, ipsum dolor.</i>)</b>", "Pisone in eo gymnasio, quod Ptolomaeum vocatur, unaque nobiscum Q. Non enim quaero quid verum, sed quid cuique dicendum sit. Dat enim intervalla et relaxat. At negat Epicurus-hoc enim vestrum lumen estquemquam, qui honeste non? <b>(Answer: iucunde posse vivere)</b>"]

# def create_activity(cpt):
#     for desc in a_desc:
#         act = Activity(description=desc, concept=cpt)
#         print(act)
#         act.save()
# for cpt in concept_objs:
#     create_activity(cpt)

# for cpt in concept_objs:
#     for act in cpt.activities:
#         print(act)
#     print()
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

# all_quizzes = storage.all(Quiz)
# for q in all_quizzes.values():
#     q.delete()
# storage.save()

# all_options = storage.all(Option)
# for op in all_options.values():
#     op.delete()
# storage.save()