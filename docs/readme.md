# Relatório de Notas de Alunos

## Descrição

Este projeto foi inspirado em uma funcionalidade que poderia ser integrada ao SIGAA, oferecendo a professores e gestores educacionais uma forma prática de gerar relatórios automatizados de desempenho acadêmico. A proposta é transformar os dados dos estudantes em uma planilha estruturada, pronta para ser analisada em ferramentas como Excel, Power BI ou Google Sheets.

O desenvolvimento seguiu os princípios do TDD (Test-Driven Development), dentro da abordagem de XP (Extreme Programming), com foco em escrever testes antes do código, garantir qualidade desde o início e manter o código limpo e sustentável.

---

### Como executar

1. **Clone o repositório**:

```bash
git clone https://github.com/gustavokubiack/xp_example.git
cd xp_example
```

2. **Crie um ambiente virtual**:

```bash
python -m venv venv
```

3. **Ative o ambiente virtual**:

* **Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```

4. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

5. **Execute o projeto**:

```bash
python  xp_example/relatorio.py
```

A planilha `relatorio.xlsx` será gerada na raiz do projeto. Foi deixado uma planilha de exemplo no repositório.

---

## Testes

Execute os testes com:

```bash
pytest
```
