document.getElementById('login-usuario').addEventListener('submit', function(e){
    e.preventDefault();

    const username = document.getElementById('nome').value;
    const password = document.getElementById('senha').value;


    let formData = new FormData();

    formData.append('username', username);
    formData.append('password', password);

    try {
        axios.post('http://127.0.0.1:8000/api/token/', formData)

        .then(response =>{

            const token = response.data.access;

            if(token != null){
                
                localStorage.setItem('token', token);

                window.location.href = './pages/menu.html'
            }
            else{
                alert('erro de token vazio');
            }
        })
        
        .catch(error =>{
            console.error(error);
            alert(error);
        })

    } catch (error) {
        console.error(error);
        alert(error);
    }



})