<?php

$dbHost = 'localhost';
$dbUsername = 'root';
$dbPaaword = '';
$dbName = 'db_polo';

$conexao = new mysqli($dbHost,$dbUsername,$dbPaaword,$dbName);

if($conexao->connect_errno)
{
    echo "ERRO";
}
else
{
    echo "Conexão efetuada com sucesso";
}

?>