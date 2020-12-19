import sqlite3
import random

name = "Nyaa"
titles = [
    "Missing Link of the Annihilator -Absolute Zero-",
    "Epigraph of the Closed Curve -Closed Epigraph-",
    "Protocol of the Two-sided Gospel -X-day Protocol-",
    "Solitude of the Mournful Flow -A Stray Sheep-",
    "Solitude of the Astigmatism -Entangled Sheep-",
    "Eclipse of Orbital Ordering -The Orbital Eclipse-",
    "Eclipse of Vibronic Transition -Vibronic Transition-",
    "Dual of Antinomy -Antinomic Dual-",
    "Pandora of Eternal Return -Pandora's Box-",
    "Pandora of Provable Existence -Forbidden Cubicle-",
    "Pandora of Forgotten Existence -Sealed Reliquary-",
    "Mother Goose of Mutual Recursion -Recursive Mother Goose-",
    "Mother Goose of Diffractive Recitativo -Diffraction Mother Goose-",
    "Recognition of the Elastic Limit -Presage or Recognize-",
    "Recognition of the Asymptotic Line -Recognize Asympote-",
    "Altair of the Point at Infinity -Vega and Altair-",
    "Altair of the Hyperbolic Plane -Beltrami Pseudosphere-",
    "Altair of Translational Symmetry -Translational Symmetry-",
    "Altair of the Cyclic Coordinate -Time-leap Machine-",
    "Rinascimento of the Unwavering Promise -Promised Rinascimento-",
    "Rinascimento of Image Formation -Return of the Phoenix-",
    "Rinascimento of Projection -Project Amadeus-",
    "Arc-light of the Point at Infinity -Arc-light of the Sky-",
]

def run():
    log = []

    conn = sqlite3.connect('torr_db.sqlite3')
    cursor = conn.cursor()

    for _ in range(5):
        episode = random.randint(1, 24)
        log += ['Ищем серию номер %s...' % episode]

        cursor.execute("select title from episodes where id = %s" % episode)
        res = cursor.fetchall()
        if len(res) == 0:
            log += ['Успешно? False']
            continue

        log += ["Успешно? True"]
        log += ["Верно? %r\n" % (res[0][0] == titles[episode - 1])]

    return log
