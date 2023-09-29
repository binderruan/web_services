# Projeto de Web Services com três aplicações distintas

<b>Cliente 1 (Sensor IoT):</b> Gera dados de temperatura, umidade e luminosidade a cada 10 segundos e envia para o Web Service.
<b>Web Service (REST ou GraphQL):</b> Recebe os dados do Cliente 1, armazena no banco de dados, permite criar, ler, atualizar e excluir informações, registrando também a data e hora das alterações.
<b>Cliente 2 (Consumidor):</b> Permite aos usuários visualizar os dados do Web Service, incluindo a leitura mais recente e a capacidade de selecionar leituras por data e hora específicas.
