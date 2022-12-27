# crtsh.py

A Python script for performing recon on a given domain using the [Certificate Transparency](https://www.certificate-transparency.org/) (CT) logs.

## Usage

```
python crtsh.py -d [domain] -o [output_file]
```

## Arguments

- `-d`: The domain to perform recon on.
- `-o`: The name of the output file. The script will write the results of the recon to this file.

## Example

```
python crtsh.py -d example.com -o example_output.txt
```

This will perform recon on `example.com` and write the results to a file called `example_output.txt`.
