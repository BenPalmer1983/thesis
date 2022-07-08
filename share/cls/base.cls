%%------------------------------------------------------------------------------
%%------------------------------------------------------------------------------


%% Load packages
\usepackage[toc,page]{appendix}
\usepackage{geometry}
\usepackage{import}
\usepackage{titlesec}
\usepackage{fancyhdr} 
\usepackage{cmap}
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
\usepackage{svg}
\usepackage{pdfpages} 
\usepackage{physics} 
\usepackage{caption}
\usepackage{subcaption}
\usepackage{lscape}
\usepackage{hyperref}
\usepackage[autostyle]{csquotes}
\usepackage{afterpage}
\newcommand\blankpage{
    \null
    \thispagestyle{empty}
    \addtocounter{page}{-1}
    \newpage
    }

% Equation packages
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{textgreek}
\usepackage[nice]{nicefrac}

% Frames
\usepackage{mdframed}

%% Bib and Referencing
\usepackage[backend=bibtex,
bibstyle=numeric,
hyperref=true,
sorting=none]{biblatex}
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
\usetikzlibrary{math}
\usepackage{tikz-feynman} 
\usetikzlibrary{positioning}

%% Tables
\usepackage{longtable}
\usepackage{tabularx}
\usepackage{adjustbox}

%% Algorithm + Pseduocode
\usepackage{algorithmicx}
\usepackage{algpseudocode}
\algdef{SE}[DOWHILE]{Do}{doWhile}{\algorithmicdo}[1]{\algorithmicwhile\ #1}%


\usepackage{placeins}

%%\usepackage{glossaries}
\usepackage[acronym]{glossaries}



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



\include{share/colours/colours}
\include{share/listings/listings}
\include{share/tikz/tikz}
%\include{share/tikz/crystals}
\include{share/equations/equations}
\include{share/code/code}
\include{share/tables/tables}




%%------------------------------------------------------------------------------
%%------------------------------------------------------------------------------
