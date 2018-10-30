@echo off
xelatex -aux-directory=latex-temp report.tex
sumatrapdf report.pdf