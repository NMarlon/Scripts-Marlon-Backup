<?php
//echo "Erro 404 - Página não encontrarda";
if ($_SERVER['PATH_INFO'] === '/listar-cursos'){
    require 'listar-cursos.php';
}
