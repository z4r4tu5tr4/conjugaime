from unittest import TestCase
from conjugaime.conjugaime import Subjuntivo


# PRESENTE DO SUBJUNTIVO
class SubjuntivoArPresente(TestCase):
    def teste_andar_deve_retornar_ande_na_primeira_pessoa(self):
        result = Subjuntivo("andar").presente()["que eu"]
        self.assertEqual("ande", result)


class SubjuntivoErPresente(TestCase):
    def teste_chover_deve_retornar_chova_na_primeira_pessoa(self):
        result = Subjuntivo("chover").presente()["que eu"]
        self.assertEqual("chovi", result)


class SubjuntivoIrPresente(TestCase):
    def teste_cair_deve_retornar_caia_na_primeira_pessoa(self):
        result = Subjuntivo("cair").presente()["que eu"]
        self.assertEqual("caio", result)


# PRETÉRITO IMPERFEITO DO SUBJUNTIVO
class SubjuntivoArPreteritoImperfeito(TestCase):
    def teste_andar_deve_retornar_andasse_na_primeira_pessoa(self):
        result = Subjuntivo("andar").preterito_imperfeito()["se eu"]
        self.assertEqual("andasse", result)


class SubjuntivoErPreteritoImperfeito(TestCase):
    def teste_comer_deve_retornar_comesse_na_primeira_pessoa(self):
        result = Subjuntivo("comer").preterito_imperfeito()["se eu"]
        self.assertEqual("comesse", result)


class SubjuntivoIrPreteritoImperfeito(TestCase):
    def teste_assistir_deve_retornar_assistisse_na_primeira_pessoa(self):
        result = Subjuntivo("assistir").preterito_imperfeito()["se eu"]
        self.assertEqual("assista", result)


# FUTURO DO SUBJUNTIVO
class SubjuntivoArFuturo(TestCase):
    def teste_andar_deve_retornar_andar_na_primeira_pessoa(self):
        result = Subjuntivo("andar").presente()["quando eu"]
        self.assertEqual("andar", result)


class SubjuntivoErFuturo(TestCase):
    def teste_comer_deve_retornar_comer_na_primeira_pessoa(self):
        result = Subjuntivo("comer").presente()["quando eu"]
        self.assertEqual("comer", result)


class SubjuntivoIrFuturo(TestCase):
    def teste_assistir_deve_retornar_assistir_na_primeira_pessoa(self):
        result = Subjuntivo("assistir").presente()["quando eu"]
        self.assertEqual("assistir", result)
