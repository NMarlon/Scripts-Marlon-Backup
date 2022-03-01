<?php

require __DIR__ . '/../vendor/autoload.php';

require __DIR__ . '/../src/MarlonDebug/dbg.php';

use Alura\Cursos\Controller\ListarCursos;
use Alura\Cursos\Controller\FormularioInsercao;


//fazer log de todas as requisições
switch ($_SERVER['PATH_INFO']) {
    case '/listar-cursos':
        $titulo='Lista De Cursos';
        $controlador = new ListarCursos();
        $controlador->processaRequisicao();
        
        break;
    case '/formulario-novo-curso':

        $titulo='Formulário';
        $controlador = new FormularioInsercao();
        $controlador->processaRequisicao();
       
        //require 'formulario-novo-curso.php';
        break;
    default:
        echo "Erro 404 - PÁGINA NÃO ENCONTRADA";    
        break;
}