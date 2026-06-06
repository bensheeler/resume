# Resume

Resume source data lives in `resume.yaml`. Generated outputs are `resume.typ` and `resume.pdf`.

After editing `resume.yaml`, rebuild the resume:

```sh
make build
```

You can also run the generator directly:

```sh
python3 build_resume.py
```

Run tests with:

```sh
make test
```
