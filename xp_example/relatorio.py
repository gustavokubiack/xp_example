from dataclasses import dataclass
from typing import List
import pandas as pd


@dataclass
class Disciplina:
    nome: str


@dataclass
class Nota:
    nota: float
    disciplina: Disciplina


@dataclass
class Aluno:
    nome: str
    notas: List[Nota]


@dataclass
class Relatorio:
    alunos: List[Aluno]

    def gerar_relatorio(self) -> pd.DataFrame:
        dados = []
        for aluno in self.alunos:
            for nota in aluno.notas:
                dados.append(
                    {
                        "Nome": aluno.nome,
                        "Disciplina": nota.disciplina.nome,
                        "Nota": nota.nota,
                        "Status": "Aprovado" if nota.nota >= 7 else "Reprovado",
                    }
                )
        return pd.DataFrame(dados)

    def formatar_relatorio(self, nome_arquivo: str = "relatorio.xlsx") -> None:
        df = self.gerar_relatorio()

        with pd.ExcelWriter(nome_arquivo, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Relatório")
            workbook = writer.book
            worksheet = writer.sheets["Relatório"]

            center_format = workbook.add_format(
                {"align": "center", "valign": "vcenter"}
            )
            float_format = workbook.add_format(
                {"num_format": "0.00", "align": "center", "valign": "vcenter"}
            )

            for idx, column in enumerate(df.columns):
                max_len = max(df[column].astype(str).map(len).max(), len(column)) + 2
                col_format = float_format if column == "Nota" else center_format
                worksheet.set_column(idx, idx, max_len, col_format)


def main():
    alunos = [
        Aluno(
            nome="Alan Turing",
            notas=[
                Nota(nota=8.5, disciplina=Disciplina(nome="Engenharia de Software")),
                Nota(nota=6.0, disciplina=Disciplina(nome="Português")),
            ],
        ),
        Aluno(
            nome="Gustavo Kubiack",
            notas=[
                Nota(nota=9.0, disciplina=Disciplina(nome="Matemática")),
                Nota(nota=7.5, disciplina=Disciplina(nome="Química")),
            ],
        ),
    ]

    relatorio = Relatorio(alunos)
    relatorio.formatar_relatorio()
    print("Relatório gerado com sucesso!")


if __name__ == "__main__":
    main()
