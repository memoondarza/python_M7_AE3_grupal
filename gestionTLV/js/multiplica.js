function precioTotal() {
  var m1 = document.getElementById("precio").value;
  var m2 = document.getElementById("cantidad").value;
/*  var calcular = document.getElementById("calcular");*/
  
  multi = m1 * m2;
  document.getElementById("calcular").innerHTML = multi;
  return 
}
precioTotal(); 

