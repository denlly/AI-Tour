var md2rst = require('markdown-to-restructuredtext');
const fs = require('fs');
const path = require('path');
const docpath = path.join(__dirname, '../docs/');

module.exports = class MakeMd {
    async find(dirname) {
        let filelist = [];
        await fs.readdir(path.join(docpath, dirname), {}, function (err, files) {
            if (err) {
                throw new TypeError(err.message);
            } else {
                filelist = files.filter((value, index) => {
                    const regExp = /^\w+(.md)$/;
                    return regExp.test(value);
                });
                filelist.map((value, index) => {
                    const fullname = path.join(docpath, dirname, value);
                    const outfile = fullname + '.rst';
                    console.log("Converted::" + fullname);
                    if (fs.existsSync(outfile)) {
                        fs.unlink(outfile);
                    }
                    md2rst(outfile, fullname, (err) => {
                        if (err) {
                            throw err;
                        }
                    });
                    //console.log(fullname);
                })
            }
        })
    }

}