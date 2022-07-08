\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{manual}[2016/06/23]

%% Load base class
\LoadClass{report}

%% Load packages
\usepackage[toc,page]{appendix}
\usepackage{geometry}
\usepackage{import}
\usepackage{titlesec}
\usepackage{cmap}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{textgreek}
\usepackage{varwidth}
\usepackage{graphicx}
\usepackage{setspace}
\usepackage[version=3]{mhchem}
\usepackage{graphicx}
\usepackage{latexsym}
\usepackage{keyval}
\usepackage{ifthen}
\usepackage{moreverb}
\usepackage{xcolor}
\usepackage{multicol}

% Frames
\usepackage{mdframed}

%% Bib and Referencing
\usepackage[backend=bibtex,
bibstyle=numeric,
hyperref=true,
sorting=none]{biblatex}
\bibliography{bib/activity.bib}     %% CHANGE BIB FILE HERE
\usepackage{notoccite}

%% Page settings
\pagenumbering{arabic}
\geometry{a4paper,total={210mm,297mm},left=20mm,right=20mm,top=20mm,bottom=20mm}

%% Margin settings
\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist

%% Paragraph settings
\usepackage{setspace}
\setlength{\parindent}{0pt}
\setlength{\parskip}{1.3ex plus 0.5ex minus 0.3ex}
\onehalfspacing
%%\doublespacing

%% Figure captions
\usepackage[font=small]{caption}

%% Make Cell
\usepackage{makecell}

%% Tikz package
\usepackage{tikz}
\usepackage{tikz-dimline}
\usetikzlibrary{shapes,arrows,3d}


%% Algorithm + Pseduocode
\usepackage{algorithmicx}
\usepackage{algpseudocode}
\algdef{SE}[DOWHILE]{Do}{doWhile}{\algorithmicdo}[1]{\algorithmicwhile\ #1}%


%%------------------------------------------------------------------------------
%%------------------------------------------------------------------------------
%% Define new commands

%% Thesis
%%-----------------------------
\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist
\newcommand{\abstractpreamble}[1]{\textit{#1}}
\newcommand{\subheadings}{\noindent\textbf}


%% Articles
%%-----------------------------
\newcommand{\R}{\mathbb{R}}



%% CVs
%%-----------------------------
\newcommand{\cvsection}[1]{\large{\bf{#1}}}
\newcommand{\cvsubsection}[1]{\normalsize{\bf{#1}}}
\newcommand{\cvtext}[1]{\normalsize{#1}}



\include{SHARED/colours/colours}
\include{SHARED/listings/listings}
\include{SHARED/tikz/tikzStyles}
\include{SHARED/tikz/crystals}





%%------------------------------------------------------------------------------
%%------------------------------------------------------------------------------