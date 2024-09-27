// const getToken = () => {
//     return localStorage.getItem('token'); // Use localStorage em vez de AsyncStorage
// };

document.getElementById('criar-usuario').addEventListener('submit', function(e){
    e.preventDefault();
    const username = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('senha').value;

    let formData = new FormData();
    formData.append('username', username);
    formData.append('email', email);
    formData.append('password', password);

    // const token = getToken();

    axios.post('http://127.0.0.1:8000/api/criarusuario/', formData, {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    .then(response =>{
        alert('Usuario criado com sucesso');
    })
    .catch(function(error){
        console.log(error);
        alert('Erro ao criar usuario');
    })






    })