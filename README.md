# Projeto PLUMA — versão Flask

Site institucional do Projeto PLUMA (Bacia da Foz do Rio Amazonas), convertido do HTML estático original para uma aplicação **Flask**.

## Estrutura de pastas

```
pluma_flask/
├── app.py                 # Aplicação Flask (rota principal "/")
├── requirements.txt       # Dependências
├── templates/
│   └── index.html         # Template Jinja2 (era o index.html estático)
└── static/
    ├── css/
    │   ├── site.css
    │   └── banner.css
    ├── js/
    │   └── site.js
    └── img/
        ├── banner-pluma.png
        └── logotipo-pluma.png
```

No Flask, o HTML fica em `templates/` e os arquivos estáticos (CSS, JS, imagens) ficam em `static/`.
No template, os caminhos usam `{{ url_for('static', filename='...') }}` em vez de caminhos relativos comuns — é assim que o Flask gera as URLs corretas para os arquivos estáticos.

## Como rodar no VSCode

1. Abra a pasta `pluma_flask` no VSCode (`Arquivo > Abrir Pasta...`).
2. Abra um terminal integrado (`Terminal > Novo Terminal`).
3. (Opcional, recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
   Ative-o:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute a aplicação:
   ```bash
   python app.py
   ```
6. Abra no navegador: **http://127.0.0.1:5000**

O servidor roda em modo debug (`debug=True`), então qualquer alteração nos arquivos recarrega a página automaticamente.

## Publicação

Para publicar em produção, não use `app.run()` diretamente. Utilize um servidor WSGI como **Gunicorn** (Linux) ou **Waitress** (Windows), por exemplo:

```bash
pip install gunicorn
gunicorn app:app
```

Serviços como Render, Railway, PythonAnywhere ou uma VPS com Nginx + Gunicorn funcionam bem para hospedar aplicações Flask.
