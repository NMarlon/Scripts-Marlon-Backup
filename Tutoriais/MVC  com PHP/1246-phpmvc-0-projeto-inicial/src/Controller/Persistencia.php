<?php

namespace Alura\Cursos\Controller;

use Alura\Cursos\Infra\EntityManagerCreator;
use Alura\Cursos\Entity\Curso;

class Persistencia implements InterfaceControladorRequisicao

	{	
		private $entityManager;
		public function __construct()
		{
			$this->entityManager =(new EntityManagerCreator())->getEntityManager();	
		}
		public function processaRequisicao(): void
		{
			//$descricao= $_POST['descricao'];
			$descricao = filter_input(INPUT_POST,'descricao',FILTER_SANITISE_STRING);
			echo $descricao;
			break;
			exit();
			$curso=new Curso();
			$curso->setDescricao($_POST['descricao']);
			$this->entityManager->persist($curso);
			$this->entityManager->flush();
			window.reaload(); 
			// code...
		}
	}
