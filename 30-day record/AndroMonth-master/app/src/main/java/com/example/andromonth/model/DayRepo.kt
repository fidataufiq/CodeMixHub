package com.example.andromonth.model

import androidx.annotation.DrawableRes
import androidx.annotation.StringRes
import com.example.andromonth.R

data class Day(
    @DrawableRes val imageRes: Int,
    @StringRes val titleRes: Int,
    @StringRes val descRes: Int
)

object DayRepo {
    val days = listOf(
        Day(R.drawable.start, R.string.title0, R.string.desc0),
        Day(R.drawable.start, R.string.title1, R.string.desc1),
        Day(R.drawable.schedule, R.string.title2, R.string.desc2),
        Day(R.drawable.group, R.string.title3, R.string.desc3),
        Day(R.drawable.hobbies, R.string.title4, R.string.desc4),
        Day(R.drawable.checklist, R.string.title5, R.string.desc5),
        Day(R.drawable.reflection, R.string.title6, R.string.desc6),
        Day(R.drawable.motivation, R.string.title7, R.string.desc7),
        Day(R.drawable.skills, R.string.title8, R.string.desc8),
        Day(R.drawable.health, R.string.title9, R.string.desc9),
        Day(R.drawable.stress, R.string.title10, R.string.desc10),
        Day(R.drawable.project, R.string.title11, R.string.desc11),
        Day(R.drawable.learn, R.string.title12, R.string.desc12),
        Day(R.drawable.lecture, R.string.title13, R.string.desc13),
        Day(R.drawable.holiday, R.string.title14, R.string.desc14),
        Day(R.drawable.finance, R.string.title15, R.string.desc15),
        Day(R.drawable.inspiration, R.string.title16, R.string.desc16),
        Day(R.drawable.open, R.string.title17, R.string.desc17),
        Day(R.drawable.self, R.string.title18, R.string.desc18),
        Day(R.drawable.self1, R.string.title19, R.string.desc19),
        Day(R.drawable.people, R.string.title20, R.string.desc20),
        Day(R.drawable.table, R.string.title21, R.string.desc21),
        Day(R.drawable.dream, R.string.title22, R.string.desc22),
        Day(R.drawable.test, R.string.title23, R.string.desc23),
        Day(R.drawable.learn, R.string.title24, R.string.desc24),
        Day(R.drawable.hiking, R.string.title25, R.string.desc25),
        Day(R.drawable.lecture, R.string.title26, R.string.desc26),
        Day(R.drawable.self, R.string.title27, R.string.desc27),
        Day(R.drawable.test, R.string.title28, R.string.desc28),
        Day(R.drawable.holiday, R.string.title29, R.string.desc29)
    )
}