const DivPai=document.querySelector(".container")
var dados_recebidos;
async function criar_carros() {
        const init={ //configurando o metodo POST para enviar um json
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({"quantidade": 20}) //Json que sera enviado
    }
    const url= await fetch("http://127.0.0.1:5000/gerar_carros", init) //carregando API, aplicando as cinfigurações
    dados_recebidos= await url.json() //Resposta recebida da API
    carregar()
}
function carregar(){
    for (const chave in dados_recebidos) {
        let local_img=dados_recebidos[chave]['_path'].replace(/\/\/+/g, '/')
        
        var DivFilho=document.createElement("div")
        DivFilho.className="carros"
        DivFilho.id=chave

        DivFilho.style.background=`url(${local_img})`
        DivFilho.style.backgroundSize='cover'

        DivPai.appendChild(DivFilho)
    }
}
function criar_arquivo(){

}
