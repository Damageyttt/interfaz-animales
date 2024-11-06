from app.model.Elefante import Elefante
from app.model.Murcielago import Murcielago
from app.model.Pato import Pato

elefante = Elefante()

print("Animales que respiran")
elefante.desplazar()

murcielago = Murcielago()
print ("animales que vuelan")
murcielago.volar()

pato = Pato()

print("Animales que nadan")
pato.nadar()