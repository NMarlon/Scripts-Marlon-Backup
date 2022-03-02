<?php


namespace Alura\Cursos\Controller;

class FormularioInsercao implements InterfaceControladorRequisicao{
	public function processaRequisicao():void{	
		$titulo='Formulário';
		require __DIR__ . '/../../view/cursos/formulario.php';
	}
}