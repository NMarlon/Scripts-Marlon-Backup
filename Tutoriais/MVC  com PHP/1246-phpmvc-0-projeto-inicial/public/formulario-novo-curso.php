
<?php 
require __DIR__ . '/../src/MarlonDebug/dbg.php';

$titulo='Formulário';
include __DIR__ . '/../view/cursos/inicio-html.php'; 

?>


    <form>
        <div class="form-group">
            <label for="descricao">Descrição</label>
            <input type="text" id="descricao" name="descricao" class="form-control">

        </div>
        <button class="btn btn-primary">Salvar</button>
    </form>


<?php include __DIR__ . '/../view/cursos/fim-html.php'; ?>
<!-- I:\Arquivos de Programas Portables\GitHub\Repositorios\Scripts-Marlon-Backup\Tutoriais\MVC  com PHP\1246-phpmvc-0-projeto-inicial


  -->