
const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
});


async function Main() {

    const filename = process.argv[2];
    console.log('filename:'+filename);

    const fs = require('fs').promises;
    const contents = await fs.readFile(filename, {encoding: 'base64'});
    // console.log(contents);

    var path = require('path');


    // doesnt work
    // TRY 1
    // contents.replace(/^data:image\/png;base64,/, '');
    // fs.writeFile(path.resolve(__dirname, './image.png'), contents, 'base64', function(err) {
    //     if (err) throw err;
    // });

    // doesnt work
    // TRY 2
    // const imageData = Buffer.from(contents, 'binary');
    // const filePath = './image1.png';
    // fs.writeFile(filePath, imageData, (err) => {
    // if (err) throw err;
    // console.log('Image saved successfully!');
    // });


}

Main();

