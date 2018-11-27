/**
 * Adicionar itens vazios com jQuery. Útil para testes rápidos no console do navegador!
 * @param {int} qtdItens 
 * @param {string} element 
 */
function addItensNullOnClick(qtdItens, element) {
  for (var i = 0; i < qtdItens; i++) {
    jQuery(element).click();
  }
}