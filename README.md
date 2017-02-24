<h2> Tutorial </h2>
<p align="justify">
Criamos esta arquitetura a partir de uma plataforma Linux (Ubuntu 14) 64 bits e Docker 1.10.3. Os  procedimentos a seguir descrevem passo a passo a configuração do ambiente e a execução do recomendador de conteúdo.
</p>
<p align="justify">
Após descarregar o projeto, entre no diretório e execute o seguinte comando para executar a build do Docker:
</p>

> docker build -t recomendador .

<p align="justify" style="padding-top: 15px;">
Certifique-se de que a build foi executada corretamente e de que todos os downloads foram executados. Agora você pode criar uma instância Docker dessa máquina. Veja:
</p>

> docker run -d -P --name recomendador recomendador

<p align="justify" style="padding-top: 15px;">
Execute o comando a seguir para descobrir a porta ssh que a instância foi disponibilizada:
</p>

> docker port recomendador

<p align="justify" style="padding-top: 15px;">
Agora você pode se conectar a instância usando ssh. A senha é: 'screencast'.
</p>

> ssh root@localhost -p ssh-port

> google-cloud-sdk/install.sh

> source ~/.bashrc

> gcloud components install core cloud-datastore-emulator gcd-emulator app-engine-python

> export GAE_HOME="/home/everton/google-cloud-sdk/platform/google_appengine"

> # Google App Engine path
> export PYTHONPATH="$GAE_HOME:$GAE_HOME/lib/:$GAE_HOME/lib/yaml/"

> # PATH
> export PATH="$PATH:/home/everton/google-cloud-sdk/platform/google_appengine"

> cp /root/google-cloud-sdk/platform/google_appengine/lib/fancy_urllib/fancy_urllib/__init__.py /root/google-cloud-sdk/platform/google_appengine/lib/fancy_urllib/__init__.py
