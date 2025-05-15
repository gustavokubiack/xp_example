import pytest
from xp_example import Relatorio, Nota, Aluno, Disciplina


@pytest.fixture
def exemplo_de_alunos():
    return [
        Aluno(
            nome="João Silva",
            notas=[
                Nota(nota=8.5, disciplina=Disciplina(nome="Matemática")),
                Nota(nota=6.0, disciplina=Disciplina(nome="História")),
            ],
        ),
        Aluno(
            nome="Maria Oliveira",
            notas=[
                Nota(nota=9.0, disciplina=Disciplina(nome="Física")),
                Nota(nota=7.5, disciplina=Disciplina(nome="Química")),
            ],
        ),
    ]


def test_gerar_relatorio_contem_todas_as_linhas(exemplo_de_alunos):
    relatorio = Relatorio(exemplo_de_alunos)
    df = relatorio.gerar_relatorio()

    assert len(df) == 4


def test_gerar_relatorio_colunas_corretas(exemplo_de_alunos):
    relatorio = Relatorio(exemplo_de_alunos)
    df = relatorio.gerar_relatorio()

    colunas_esperadas = {"Nome", "Disciplina", "Nota", "Status"}
    assert colunas_esperadas == set(df.columns)


def test_gerar_relatorio_status_aprovacao(exemplo_de_alunos):
    relatorio = Relatorio(exemplo_de_alunos)
    df = relatorio.gerar_relatorio()

    status_esperado = ["Aprovado", "Reprovado", "Aprovado", "Aprovado"]
    assert list(df["Status"]) == status_esperado


def test_gerar_relatorio_valores_corretos(exemplo_de_alunos):
    relatorio = Relatorio(exemplo_de_alunos)
    df = relatorio.gerar_relatorio()

    assert df.iloc[0]["Nome"] == "João Silva"
    assert df.iloc[0]["Disciplina"] == "Matemática"
    assert df.iloc[0]["Nota"] == 8.5
    assert df.iloc[0]["Status"] == "Aprovado"
