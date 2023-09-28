import React, {useState} from 'react'

const App = () => {
    const [url, setUrl] = useState("");
    const [image, setImage] = useState("");

    const buttonOnClick = () => {
        fetch(`http://127.0.0.1:8000/api/getImage?url=${url}`)
            .then(response => response.json())
            .then(json => setImage(json));

        fetch(`http://127.0.0.1:8000/api/getGenre?url=${url}`)
            .then(response => response.json())
            .then(json => console.log(json));
    }

    return (
        <div className="flex h-screen">
            <div className="grid grid-cols-3 justify-items-center items-center m-auto">
                <input
                    type="text"
                    placeholder="Insira o link de uma música do Spotify"
                    className="input input-bordered w-full max-w-xs col-span-2"
                    onChange={(e) => setUrl(e.target.value)}
                />
                <div className="avatar row-span-2">
                  <div className="w-64 rounded">
                    <img src={image} />
                  </div>
                </div>
                <button className="btn" onClick={buttonOnClick}>Buscar</button>
            </div>
        </div>
    );
}

export default App