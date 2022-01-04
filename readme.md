# Try it all

Appunti su come creare un'app desktop di ricerca avanzata di openmlol.

## Filosofia: la base teorica

Per ora la app funziona solo "in lettura", quindi è più sensato sfruttare le capacità di calcolo di Solr.
L'endpoint è: https://search-3.medialibrary.it/solr/openmlol/select, in produzione

Per le prove utilizzare https://search-2.medialibrary.it/solr/openmlol/select, dati non aggiornati, ma non si carica il server di produzione.

NOTA: su pysolr togliere "/select" (chiedere a Raffaele quando torna)

[pysolr](https://pypi.org/project/pysolr/2.1.0/) potrebbe essere una libreria adatta alla creazione di query tramite python.

Per la parte app, utilizzo di Flask e Jinja2 (per templating). Una breve guida di inizio qui: [https://realpython.com/primer-on-jinja-templating/](https://realpython.com/primer-on-jinja-templating/)

Vedi anche per Flask in generale [https://pythonhow.com/building-a-website-with-python-flask/](https://pythonhow.com/building-a-website-with-python-flask/)

Form in flask: [https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/](https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/)

Thanks to https://github.com/spawnmarvel/solrhttp for architecture help


https://towardsdatascience.com/create-a-full-search-engine-via-flask-elasticsearch-javascript-d3js-and-bootstrap-275f9dc6efe1
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-full-text-search
https://medium.com/@joseortizcosta/search-utility-with-flask-and-mysql-60bb8ee83dad
https://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/

Get e Post: https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests


Sass and Flask: https://sass.github.io/libsass-python/frameworks/flask.html

Jinja2 template: https://jinja.palletsprojects.com/en/2.11.x/templates/

python and javascript in flask: https://www.jitsejan.com/python-and-javascript-in-flask.html

<!-- iterate results
        {% for r in data %}
        <p> {{ r }}</p>
        {% endfor %}
        <br>
-->

arguments lists: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html

form in bootstrap: https://getbootstrap.com/docs/4.0/components/forms/

some javascript thing: https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onchange

https://medium.com/@avremelk/solr-gottchas-a-tutorial-a953c8b3e775

multiple select? https://www.soengsouy.com/2020/03/bootstrap-4-multiselect-dropdown.html?m=1

Used flask-pagination: https://flask-paginate.readthedocs.io/en/master/
