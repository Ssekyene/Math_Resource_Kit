from models import storage
from models.concept import Concept

numbers = Concept(name="Numbers", introduction="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Multoque hoc melius nos veriusque quam Stoici. Quoniam, si dis placet, ab Epicuro loqui discimus. Respondent extrema primis, media utrisque, omnia omnibus. Haec para/doca illi, nos admirabilia dicamus. Cum autem in quo sapienter dicimus, id a primo rectissime dicitur. Duo Reges: constructio interrete. Et ille ridens: Video, inquit, quid agas; Ergo adhuc, quantum equidem intellego, causa non videtur fuisse mutandi nominis.", conclusion="Equidem, sed audistine modo de Carneade? Quis enim redargueret? Dulce amarum, leve asperum, prope longe, stare movere, quadratum rotundum. Collige omnia, quae soletis: Praesidium amicorum. At eum nihili facit; Etenim semper illud extra est, quod arte comprehenditur. Inscite autem medicinae et")

print(numbers)
numbers.save()
