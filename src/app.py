from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    tableau_embed_code = """
    <div class='tableauPlaceholder' id='viz1772985097664' style='position: relative'><noscript><a href='#'><img alt='Impact of COVID-19 on India’s Power Grid: A 2019-2020 Analysis ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sk&#47;Skillwallet-Project-MSE-1&#47;ImpactofCOVID-19onIndiasPowerGridA2019-2020Analysis&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Skillwallet-Project-MSE-1&#47;ImpactofCOVID-19onIndiasPowerGridA2019-2020Analysis' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sk&#47;Skillwallet-Project-MSE-1&#47;ImpactofCOVID-19onIndiasPowerGridA2019-2020Analysis&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1772985097664');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1200px';vizElement.style.height='827px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en" class="scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EnergyGrid Analytics | B.Tech Project</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        
        <script>
            tailwind.config = {{
                theme: {{
                    extend: {{
                        fontFamily: {{ sans: ['"Plus Jakarta Sans"', 'sans-serif'] }},
                        colors: {{
                            background: '#05050A',
                            surface: 'rgba(255, 255, 255, 0.03)',
                            primary: '#00D2FF',
                            secondary: '#3A7BD5'
                        }}
                    }}
                }}
            }}
        </script>
        <style>
            body {{
                background-color: #05050A;
                color: #E2E8F0;
                /* Subtle dot matrix background for data engineering vibe */
                background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
                background-size: 24px 24px;
            }}
            /* Glowing orb effect behind the dashboard */
            .glow-bg {{
                position: absolute;
                top: 20%;
                left: 50%;
                transform: translateX(-50%);
                width: 70vw;
                height: 50vh;
                background: radial-gradient(circle, rgba(58,123,213,0.15) 0%, rgba(0,210,255,0.05) 50%, transparent 70%);
                filter: blur(80px);
                z-index: -1;
                pointer-events: none;
            }}
            .glass-panel {{
                background: rgba(15, 15, 20, 0.6);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 1rem;
            }}
            .text-gradient {{
                background: linear-gradient(135deg, #FFFFFF 0%, #A0AEC0 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            .accent-gradient {{
                background: linear-gradient(135deg, #00D2FF 0%, #3A7BD5 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            /* Precision wrapper for 1200x800 Tableau Story */
            .tableau-frame {{
                width: 1200px;
                height: 800px;
                background: #FFFFFF; /* Tableau base color */
                border-radius: 0.75rem;
                overflow: hidden;
            }}
            .tableau-frame iframe {{
                width: 100% !important;
                height: 100% !important;
                border: none !important;
            }}
            /* Animated gradient border for the dashboard */
            .gradient-border-wrapper {{
                padding: 1px;
                background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(0, 210, 255, 0.4), rgba(255,255,255,0.1));
                border-radius: 0.85rem;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
            }}
        </style>
    </head>
    <body class="min-h-screen relative pb-20 selection:bg-blue-500/30">
        <div class="glow-bg"></div>

        <nav class="fixed top-0 left-0 right-0 z-50 px-6 py-4">
            <div class="max-w-[1240px] mx-auto glass-panel px-6 py-3 flex justify-between items-center shadow-lg">
                <div class="flex items-center gap-3">
                    <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-[#3A7BD5] to-[#00D2FF] p-[1px]">
                        <div class="w-full h-full bg-[#05050A] rounded-lg flex items-center justify-center">
                            <svg class="w-5 h-5 text-[#00D2FF]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        </div>
                    </div>
                    <span class="font-bold text-lg tracking-wide text-white">EnergyGrid<span class="text-[#00D2FF]">.ai</span></span>
                </div>
                <div class="flex gap-4 items-center">
                    <div class="hidden md:flex gap-2 items-center">
    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-[11px] font-semibold tracking-wide text-gray-300 shadow-inner">
        <span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
        PYTHON
    </div>
    
    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-[11px] font-semibold tracking-wide text-gray-300 shadow-inner">
        <span class="w-1.5 h-1.5 rounded-full bg-orange-400"></span>
        MYSQL
    </div>
    
    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-[11px] font-semibold tracking-wide text-gray-300 shadow-inner">
        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400"></span>
        TABLEAU
    </div>

    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-[11px] font-semibold tracking-wide text-gray-300 shadow-inner">
        <span class="w-1.5 h-1.5 rounded-full bg-gray-400"></span>
        FLASK
    </div>
</div>
                </div>
            </div>
        </nav>

        <div class="max-w-[1240px] mx-auto px-6 pt-32 mt-4">
            
            <header class="text-center mb-16 space-y-4">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-medium mb-4">
                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                    End-to-End Analytics Pipeline
                </div>
                <h1 class="text-5xl md:text-6xl font-extrabold tracking-tight text-white mb-6">
                    COVID-19 Power <br/> <span class="accent-gradient">Consumption Impact</span>
                </h1>
                <p class="text-lg text-gray-400 max-w-2xl mx-auto leading-relaxed">
                    An interactive data engineering analysis of India's electricity demand, tracking the transition from pre-pandemic baselines through the 2020 lockdowns and regional recoveries.
                </p>
            </header>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16 relative z-10">
                <div class="glass-panel p-6 hover:border-[#00D2FF]/40 transition-colors duration-300 group">
                    <div class="flex justify-between items-start mb-4">
                        <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">Data Volume</span>
                        <div class="p-2 rounded-lg bg-blue-500/10 text-blue-400 group-hover:bg-blue-500/20 transition-colors">
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
                        </div>
                    </div>
                    <span class="text-3xl font-extrabold text-white block mb-1">23,000+ <span class="text-lg text-gray-500 font-medium">Rows</span></span>
                    <span class="text-sm text-gray-400">Processed via Pandas & SQL</span>
                </div>
                
                <div class="glass-panel p-6 hover:border-[#00D2FF]/40 transition-colors duration-300 group">
                    <div class="flex justify-between items-start mb-4">
                        <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">Analysis Window</span>
                        <div class="p-2 rounded-lg bg-purple-500/10 text-purple-400 group-hover:bg-purple-500/20 transition-colors">
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                        </div>
                    </div>
                    <span class="text-3xl font-extrabold text-white block mb-1">Jan '19 – Dec '20</span>
                    <span class="text-sm text-gray-400">Time-series data filtered for accuracy</span>
                </div>

                <div class="glass-panel p-6 hover:border-[#00D2FF]/40 transition-colors duration-300 group">
                    <div class="flex justify-between items-start mb-4">
                        <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">Story Scenes</span>
                        <div class="p-2 rounded-lg bg-emerald-500/10 text-emerald-400 group-hover:bg-emerald-500/20 transition-colors">
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
                        </div>
                    </div>
                    <span class="text-3xl font-extrabold text-white block mb-1">3 Scenarios</span>
                    <span class="text-sm text-gray-400">National Trend, Regional, & Recovery</span>
                </div>
            </div>

            <div class="glass-panel p-8 mt-12 mb-12 relative z-10 hover:border-[#00D2FF]/40 transition-colors duration-300">
    
    <div class="flex items-center justify-center gap-3 mb-8">
        <div class="w-8 h-8 rounded bg-red-500/10 border border-red-500/20 flex items-center justify-center text-red-400 shadow-lg shadow-red-500/20">
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg>
        </div>
        <h2 class="text-3xl font-bold text-white tracking-wide">Project Explanation Video</h2>
    </div>
    
    <div class="max-w-4xl mx-auto aspect-video rounded-xl overflow-hidden border border-white/10 shadow-2xl shadow-black/60 ring-1 ring-white/5">
        <iframe 
            class="w-full h-full" 
            src="https://www.youtube.com/embed/gHcxB4jhdjU"
            title="Project Demo" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    </div>
</div>

                

            <div class="flex justify-center mb-24 relative z-10">
                <div class="gradient-border-wrapper">
                    <h2 class="text-3xl font-bold text-white tracking-wide flex items-center justify-center m-3">Tableau Story and Dashboards</h2>
                    <div class="tableau-frame shadow-inner">
                        {tableau_embed_code}
                    </div>
                </div>
            </div>

            <section class="glass-panel p-10 relative z-10 overflow-hidden">
                <div class="absolute top-0 right-0 w-64 h-64 bg-blue-500/5 rounded-full blur-3xl -mr-20 -mt-20"></div>
                
                <h2 class="text-2xl font-bold mb-8 text-white flex items-center gap-3">
                    <svg class="w-6 h-6 text-[#00D2FF]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                    Project Architecture
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
                    <div class="relative pl-6 border-l border-blue-500/20">
                        <div class="absolute w-3 h-3 bg-[#00D2FF] rounded-full -left-[6.5px] top-1.5 shadow-[0_0_10px_#00D2FF]"></div>
                        <h3 class="text-base font-bold text-gray-100 mb-3">01. Data Engineering</h3>
                        <p class="text-sm text-gray-400 leading-relaxed font-light">Extracted daily Mega Unit (MU) metrics from 2013-2024. Cleaned and melted 30+ state columns into a relational format using Python Pandas, then migrated to a MySQL schema for high-speed indexing.</p>
                    </div>
                    
                    <div class="relative pl-6 border-l border-blue-500/20">
                        <div class="absolute w-3 h-3 bg-[#00D2FF] rounded-full -left-[6.5px] top-1.5 shadow-[0_0_10px_#00D2FF]"></div>
                        <h3 class="text-base font-bold text-gray-100 mb-3">02. Visual Analytics</h3>
                        <p class="text-sm text-gray-400 leading-relaxed font-light">Engineered custom Tableau calculated fields (Lockdown Phases, Region Groups) to power cross-dashboard filtering. Designed a 3-scene narrative demonstrating economic elasticity.</p>
                    </div>
                    
                    <div class="relative pl-6 border-l border-transparent"> <div class="absolute w-3 h-3 bg-[#00D2FF] rounded-full -left-[6.5px] top-1.5 shadow-[0_0_10px_#00D2FF]"></div>
                        <h3 class="text-base font-bold text-gray-100 mb-3">03. Web Deployment</h3>
                        <p class="text-sm text-gray-400 leading-relaxed font-light">Embedded the final analytical story into a lightweight, responsive Flask web application utilizing Tailwind CSS, ensuring accessibility and a seamless, interactive user experience.</p>
                    </div>
                </div>
            </section>

        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)