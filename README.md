# DemoQA - Automação de Testes (API, Web e Postman)

Este projeto reúne automações de testes para o site [DemoQA](https://demoqa.com) utilizando Python (API e Web) e Postman (coleção de testes). Ideal para validar funcionalidades tanto via interface quanto via API.

## Estrutura do Projeto

- `demoqa_api/` — Testes automatizados da API DemoQA com Python, pytest e requests
- `demoqa_web/` — Testes automatizados da interface DemoQA com Python, Selenium, pytest e Faker
- `demoqa_postman/` — Coleção de testes para API DemoQA no Postman

## Instalação

Clone o repositório:

```bash
git clone https://github.com/douglascpacheco/DemoQA.git
cd DemoQA
```

### API (Python)

```bash
cd demoqa_api
pip install -r requirements.txt
pytest tests/
```

### Web (Python)

```bash
cd demoqa_web
pip install -r requirements.txt
pytest tests/
```

### Postman

1. Instale o [Postman](https://www.postman.com/downloads/).
2. Importe `DemoQA.postman_collection.json` e `Teste.postman_environment.json`.
3. Configure a variável `URLBase` para `https://demoqa.com`.
4. Execute os testes conforme a ordem da coleção.

## Principais Ferramentas e Bibliotecas

- Python 3.x
- pytest
- requests
- selenium
- webdriver-manager
- faker
- Postman

## Estrutura de Pastas

```
demoqa_api/         # Testes de API
  ├── utils/
  ├── tests/
  ├── requirements.txt
demoqa_web/         # Testes de interface web
  ├── tests/
  ├── requirements.txt
  └── uploads/
demoqa_postman/     # Coleção e ambiente Postman
  ├── DemoQA.postman_collection.json
  └── Teste.postman_environment.json
```

## Observações

- Os testes web utilizam o ChromeDriver, gerenciado pelo webdriver-manager. Certifique-se de que o Chrome está instalado.
- Os scripts de Postman validam status code e extraem variáveis automaticamente.
- O projeto é modular: cada pasta pode ser usada separadamente conforme a necessidade.

---

Desenvolvido por [douglascpacheco](https://github.com/douglascpacheco)
