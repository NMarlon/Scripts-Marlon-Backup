<?php
 
require __DIR__ . '/../vendor/autoload.php';

require __DIR__ . '/../src/MarlonDebug/dbg.php';

use Alura\Cursos\Controller\ListarCursos;
use Alura\Cursos\Controller\FormularioInsercao;
use Alura\Cursos\Controller\Persistencia;

//fazer log de todas as requisições
switch ($_SERVER['PATH_INFO']) {

    case '/listar-cursos':
        $titulo='Lista De Cursos';
        $controlador = new ListarCursos();
        $controlador->processaRequisicao();       
        break;

    case '/novo-curso':
        $titulo='Formulário';
        $controlador = new FormularioInsercao();
        $controlador->processaRequisicao();
        break;
    case '/salvar-curso':
        $controlador = new Persistencia();
        $controlador->processaRequisicao();
        break;
    default:
        echo "Erro 404 - PÁGINA NÃO ENCONTRADA";    
        break;
}