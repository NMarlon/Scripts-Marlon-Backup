<?php

require __DIR__ . '/../vendor/autoload.php';

use Alura\Cursos\Controller\ListarCursos;
use Alura\Cursos\Controller\FormularioDeInsercao;


//fazer log de todas as requisições
switch ($_SERVER['PATH_INFO']) {
    case '/listar-cursos':
        $controlador = new ListarCursos();
        $controlador->processaRequisicao();
        $titulo='Lista De Cursos'
        break;
    case '/formulario-novo-curso':

        $controlador = new FormularioInsercao();
        $controlador->processaRequisicao();

        //require 'formulario-novo-curso.php';
        break;
    default:
        echo "Erro 404 - PÁGINA NÃO ENCONTRADA";    
        break;
}