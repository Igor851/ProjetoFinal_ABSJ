
function Calcular(){
    var divElement1 = document.getElementById('n1')
    var divElement2 = document.getElementById('n2')
    var divElement3 = document.getElementById('n3')
    var divElement4 = document.getElementById('n4')
    var n1 = divElement1.textContent.trim()
    var n2 = divElement2.textContent.trim()
    var n3 = divElement3.textContent.trim()
    var n4 = divElement4.textContent.trim()
    n1 = parseInt(n1)
    n2 = parseInt(n2)
    n3 = parseInt(n3)
    n4 = parseInt(n4)
    // var tipo = typeof(n1)
    var soma = (n1 + n2 + n3 + n4)/4
    var status 
    if (soma >= 7.0){
        status = 'Aprovado'
    }else{
        status = 'Reprovado'
    }

    document.getElementById('resultado').innerHTML = 'A média final do aluno é ' + soma + ' e este aluno está ' + status
}



