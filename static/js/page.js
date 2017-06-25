function showInserir(){
 $("#divInserir").toggle();
 $("#divCalculos").hide();
 $("#divProduzir").hide();
}
function showCalculos(){
  $("#divCalculos").toggle();
  $("#divInserir").hide();
  $("#divProduzir").hide();
}
function showProduzir(){
  $("#divProduzir").toggle();
  $("#divCalculos").hide();
  $("#divInserir").hide();
}

// controlar rows tabela Inserir



}
function calculateGrandTotal() {
    var grandTotal = 0;
    $("table.order-list").find('input[name^="price"]').each(function () {
        grandTotal += +$(this).val();
    });
    $("#grandtotal").text(grandTotal.toFixed(2));
}

// fim controlar rows tabela Inserir
