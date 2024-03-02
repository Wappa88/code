function showSum(){
  const numOne = parseInt(document.getElementById("numOne").value);
  const numTwo = parseInt(document.getElementById("numTwo").value);
  const addition = numOne + numTwo;
  document.getElementById("result").textContent = `Addition: ${addition}`;
}

function showDiv(){
  const numOne = parseInt(document.getElementById("numOne").value);
  const numTwo = parseInt(document.getElementById("numTwo").value);
  const division = numOne / numTwo;
  const remain = numOne % numTwo;
  document.getElementById("result").textContent = `Division: ${division} and remaining ${remain}`;
}

function showSub(){
  const numOne = parseInt(document.getElementById("numOne").value);
  const numTwo = parseInt(document.getElementById("numTwo").value);
  const subtraction = numOne - numTwo;
  document.getElementById("result").textContent = `Subtraction: ${subtraction}`;
}

function showMul(){
  const numOne = parseInt(document.getElementById("numOne").value);
  const numTwo = parseInt(document.getElementById("numTwo").value);
  const multiple = numOne * numTwo;
  document.getElementById("result").textContent = `Multiple: ${multiple}`;
}