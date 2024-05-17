from streamlit_elements import elements, mui, html, nivo, dashboard
import streamlit as st

# with mui.Paper:
#     with mui.Typography:
#         html.h1("Streamlit-elements使用案例",
#             css={
#                 "backgroundColor": "#00ccff",
#                 "color": "white",
#                 "borderRadius": "5px",
#                 "zIndex": 'tooltip',
#                 "height": "45px",
#                 "&:hover": {
#                     "color": "lightgreen"
#                 }
#             })
with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

    # with elements("dashboard"):
    #
    #     # First, build a default layout for every element you want to include in your dashboard
    #
    #     layout = [
    #         dashboard.Item("first_item", 0, 0, 5, 5),
    #         dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
    #         dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    #     ]
    #
    #     DATA = [
    #         {"taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114},
    #         {"taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72},
    #         {"taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99},
    #         {"taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30},
    #         {"taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103},
    #     ]
    #     def handle_layout_change(updated_layout):
    #         # You can save the layout in a file, or do anything you want with it.
    #         # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
    #         print(updated_layout)
    #
    #
    #     with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
    #         nivo.Radar(
    #             data=DATA,
    #             keys=["chardonay", "carmenere", "syrah"],
    #             indexBy="taste",
    #             valueFormat=">-.2f",
    #             margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
    #             borderColor={"from": "color"},
    #             gridLabelOffset=36,
    #             dotSize=10,
    #             dotColor={"theme": "background"},
    #             dotBorderWidth=2,
    #             motionConfig="wobbly",
    #             legends=[
    #                 {
    #                     "anchor": "top-left",
    #                     "direction": "column",
    #                     "translateX": -50,
    #                     "translateY": -40,
    #                     "itemWidth": 80,
    #                     "itemHeight": 20,
    #                     "itemTextColor": "#999",
    #                     "symbolSize": 12,
    #                     "symbolShape": "circle",
    #                     "effects": [
    #                         {
    #                             "on": "hover",
    #                             "style": {
    #                                 "itemTextColor": "#000"
    #                             }
    #                         }
    #                     ]
    #                 }
    #             ],
    #             theme={
    #                 "background": "#FFFFFF",
    #                 "textColor": "#31333F",
    #                 "tooltip": {
    #                     "container": {
    #                         "background": "#FFFFFF",
    #                         "color": "#31333F",
    #                     }
    #                 }
    #             }
    #         )
    #         mui.Paper("Second item (cannot drag)", key="second_item")
    #         mui.Paper("Third item (cannot resize)", key="third_item")

    # with elements("dashboard"):
    # First, build a default layout for every element you want to include in your dashboard


    # layout = [
    #     # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
    #     dashboard.Item("first_item", 5, 5, 10, 10),
    #     dashboard.Item("second_item", 2, 0, 10, 10),
    #     dashboard.Item("third_item", 0, 2, 10, 10),
    # ]
    # DATA = [
    #     { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
    #     { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
    #     { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
    #     { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
    #     { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    # ]
    #
    # # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # # as first parameter, plus additional properties you can find in the GitHub links below.
    #
    # with dashboard.Grid(layout):
    #     nivo.Radar(
    #         data=DATA,
    #         keys=["chardonay", "carmenere", "syrah"],
    #         indexBy="taste",
    #         valueFormat=">-.2f",
    #         margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
    #         borderColor={"from": "color"},
    #         gridLabelOffset=36,
    #         dotSize=10,
    #         dotColor={"theme": "background"},
    #         dotBorderWidth=2,
    #         motionConfig="wobbly",
    #         legends=[
    #             {
    #                 "anchor": "top-left",
    #                 "direction": "column",
    #                 "translateX": -50,
    #                 "translateY": -40,
    #                 "itemWidth": 80,
    #                 "itemHeight": 20,
    #                 "itemTextColor": "#999",
    #                 "symbolSize": 12,
    #                 "symbolShape": "circle",
    #                 "effects": [
    #                     {
    #                         "on": "hover",
    #                         "style": {
    #                             "itemTextColor": "#000"
    #                         }
    #                     }
    #                 ]
    #             }
    #         ],
    #         theme={
    #             "background": "#FFFFFF",
    #             "textColor": "#31333F",
    #             "tooltip": {
    #                 "container": {
    #                     "background": "#FFFFFF",
    #                     "color": "#31333F",
    #                 }
    #             }
    #         }
    #     )

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    # def handle_layout_change(updated_layout):
    #     # You can save the layout in a file, or do anything you want with it.
    #     # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
    #     print(updated_layout)
    #
    # with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
    #     mui.Paper("First item", key="first_item")
    #     mui.Paper("Second item (cannot drag)", key="second_item")
    #     mui.Paper("Third item (cannot resize)", key="third_item")



    # Streamlit Elements includes 45 dataviz components powered by Nivo.

    from streamlit_elements import nivo, mui

    # DATA = [
    #     { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
    #     { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
    #     { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
    #     { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
    #     { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    # ]

    # with mui.Box(sx={"height": 500}):
        # nivo.Radar(
        #     data=DATA,
        #     keys=[ "chardonay", "carmenere", "syrah" ],
        #     indexBy="taste",
        #     valueFormat=">-.2f",
        #     margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
        #     borderColor={ "from": "color" },
        #     gridLabelOffset=36,
        #     dotSize=10,
        #     dotColor={ "theme": "background" },
        #     dotBorderWidth=2,
        #     motionConfig="wobbly",
        #     legends=[
        #         {
        #             "anchor": "top-left",
        #             "direction": "column",
        #             "translateX": -50,
        #             "translateY": -40,
        #             "itemWidth": 80,
        #             "itemHeight": 20,
        #             "itemTextColor": "#999",
        #             "symbolSize": 12,
        #             "symbolShape": "circle",
        #             "effects": [
        #                 {
        #                     "on": "hover",
        #                     "style": {
        #                         "itemTextColor": "#000"
        #                     }
        #                 }
        #             ]
        #         }
        #     ],
        #     theme={
        #         "background": "#FFFFFF",
        #         "textColor": "#31333F",
        #         "tooltip": {
        #             "container": {
        #                 "background": "#FFFFFF",
        #                 "color": "#31333F",
        #             }
        #         }
        #     }
        # )
    layout = [
        dashboard.Item("Chart 1", 0, 0, 5, 3),
        dashboard.Item("Chart 2", 6, 0, 7, 3),

        dashboard.Item("曲线图", 0, 2, 6, 3),
        dashboard.Item("柱状图", 6, 2, 6, 3),

        dashboard.Item("雷达图", 0, 4, 5, 4),
        dashboard.Item("饼图", 6, 4, 7, 4),
    ]

    with elements("demo"):
        with mui.Paper:
            with mui.Typography:
                html.h1("Streamlit-elements使用案例",
                        css={
                            "backgroundColor": "#00ccff",
                            "color": "white",
                            "borderRadius": "5px",
                            "zIndex": 'tooltip',
                            "height": "45px",
                            "&:hover": {
                                "color": "lightgreen"
                            }
                        })
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        with mui.Card(key="Chart 1",
                      sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex",
                          'borderRadius': 2, "flexDirection": "column"}):
            mui.CardHeader(title="曲线图", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Pie(
                    data=[
                        {
                            "id": "TotalCarbonFootprint",
                            "label": "TotalCarbonFootprint",
                            "value": TotalCarbonFootprint,
                            "color": "hsl(354, 70%, 50%)"
                        },
                        {
                            "id": "TotalCarbonOffset",
                            "label": "TotalCarbonOffset",
                            "value": TotalCarbonOffset,
                            "color": "hsl(99, 70%, 50%)"
                        }
                    ],
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    innerRadius={0.5},
                    cornerRadius={6},
                    padAngle={0.7},
                    activeOuterRadiusOffset={8},
                    borderWidth={1},
                    borderColor={
                        "from": 'color',
                        "modifiers": [
                            [
                                'darker',
                                0.2
                            ]
                        ]
                    },
                    arcLinkLabelsSkipAngle={10},
                    arcLinkLabelsTextColor="#333333",
                    arcLinkLabelsThickness={2},
                    arcLinkLabelsColor={"from": 'color'},
                    arcLabelsSkipAngle={10},
                    arcLabelsTextColor={
                        "from": 'color',
                        "modifiers": [
                            [
                                'darker',
                                2
                            ]
                        ]
                    },
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ],
                    theme={
                        "background": "#F0FFFF",
                        "textColor": "white",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#31333F",
                            }
                        }
                    }
                )
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        with mui.Card(key="Chart 2",
                      sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex",
                          'borderRadius': 2, "flexDirection": "column"}):
            mui.CardHeader(title="曲线图", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Line(
                    data=[
                        {
                            "id": "japan",
                            "color": "hsl(272, 70%, 50%)",
                            "data": [
                                {
                                    "x": "2019",
                                    "y": 70
                                },
                                {
                                    "x": "2020",
                                    "y": 40
                                },
                                {
                                    "x": "2021",
                                    "y": 56
                                },
                                {
                                    "x": "2022",
                                    "y": 49
                                },

                            ]
                        }, ],
                    margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                    xScale={"type": 'point'},
                    yScale={
                        "type": 'linear',
                        "min": 'auto',
                        "max": 'auto',
                        "stacked": True,
                        "reverse": False
                    },
                    yFormat=" >-.2f",
                    axisTop=None,
                    axisRight=None,
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": 'Year',
                        "legendOffset": 36,
                        "legendPosition": 'middle',
                        "truncateTickAt": 0
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": 'Ton/Co2',
                        "legendOffset": -40,
                        "legendPosition": 'middle',
                        "truncateTickAt": 0
                    },
                    pointSize=10,
                    pointColor={"theme": 'background'},
                    pointBorderWidth=2,
                    pointBorderColor={"from": 'serieColor'},
                    pointLabel="data.yFormatted",
                    pointLabelYOffset=-12,
                    enableTouchCrosshair=True,
                    useMesh=True,
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ],
                    #     theme={
                    #         "background": "#F0FFFF",
                    #         "textColor": "white",
                    #         "tooltip": {
                    #             "container": {
                    #                 "background": "#FFFFFF",
                    #                 "color": "#31333F",
                    #             }
                    #         }
                    #     }
                )

            with mui.Card(key="Graph 2",
                          sx={"color": 'white', 'bgcolor': '#F0FFFF', "display": "flex",
                              'borderRadius': 2,
                              "flexDirection": "column"}):
                mui.CardHeader(title="Graph 2", className="draggable")
                with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                    nivo.Line(
                        data=dataLine,
                        margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                        xScale={"type": 'point'},
                        yScale={
                            "type": 'linear',
                            "min": 'auto',
                            "max": 'auto',
                            "stacked": True,
                            "reverse": False
                        },
                        yFormat=" >-.2f",
                        axisTop=None,
                        axisRight=None,
                        axisBottom={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": 'Year',
                            "legendOffset": 36,
                            "legendPosition": 'middle',
                            "truncateTickAt": 0
                        },
                        axisLeft={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": 'Ton/Co2',
                            "legendOffset": -40,
                            "legendPosition": 'middle',
                            "truncateTickAt": 0
                        },
                        pointSize=10,
                        pointColor={"theme": 'background'},
                        pointBorderWidth=2,
                        pointBorderColor={"from": 'serieColor'},
                        pointLabel="data.yFormatted",
                        pointLabelYOffset=-12,
                        enableTouchCrosshair=True,
                        useMesh=True,
                        legends=[
                            {
                                "anchor": "top-left",
                                "direction": "column",
                                "translateX": -50,
                                "translateY": -40,
                                "itemWidth": 80,
                                "itemHeight": 20,
                                "itemTextColor": "#999",
                                "symbolSize": 12,
                                "symbolShape": "circle",
                                "effects": [
                                    {
                                        "on": "hover",
                                        "style": {
                                            "itemTextColor": "#000"
                                        }
                                    }
                                ]
                            }
                        ],
                        #     theme={
                        #         "background": "#F0FFFF",
                        #         "textColor": "white",
                        #         "tooltip": {
                        #             "container": {
                        #                 "background": "#FFFFFF",
                        #                 "color": "#31333F",
                        #             }
                        #         }
                        #     }
                    )
        with dashboard.Grid(layout):
            dataBar = [
                {
                    "country": "AD",
                    "hot dog": 7,
                    "hot dogColor": "hsl(112, 70%, 50%)",
                    "burger": 183,
                    "burgerColor": "hsl(26, 70%, 50%)",
                    "sandwich": 189,
                    "sandwichColor": "hsl(77, 70%, 50%)",
                    "kebab": 197,
                    "kebabColor": "hsl(84, 70%, 50%)",
                    "fries": 145,
                    "friesColor": "hsl(43, 70%, 50%)",
                    "donut": 44,
                    "donutColor": "hsl(212, 70%, 50%)"
                }
            ]
            with mui.Card(key="Graph 3",
                          sx={"color": 'white', 'bgcolor': '#AFE1AF', "display": "flex",
                              'borderRadius': 2,
                              "flexDirection": "column"}):
                mui.CardHeader(title="Proportion", className="draggable")
                with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                    nivo.Bar(
                        nivo.Bar(
                            data=dataBar,
                            keys=[
                                'hot dog',
                                'burger',
                                'sandwich',
                                'kebab',
                                'fries',
                                'donut'
                            ],
                            indexBy="country",
                            margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                            padding=0.3,
                            valueScale={"type": 'linear'},
                            indexScale={"type": 'band', "round": True},
                            colors={"scheme": 'nivo'},
                            defs=[
                                {
                                    "id": 'dots',
                                    "type": 'patternDots',
                                    "background": 'inherit',
                                    "color": '#38bcb2',
                                    "size": 4,
                                    "padding": 1,
                                    "stagger": True
                                },
                                {
                                    "id": 'lines',
                                    "type": 'patternLines',
                                    "background": 'inherit',
                                    "color": '#eed312',
                                    "rotation": -45,
                                    "lineWidth": 6,
                                    "spacing": 10
                                }
                            ],
                            fill=[
                                {
                                    "match": {
                                        "id": 'fries'
                                    },
                                    "id": 'dots'
                                },
                                {
                                    "match": {
                                        "id": 'sandwich'
                                    },
                                    "id": 'lines'
                                }
                            ],
                            borderColor={
                                "from": 'color',
                                "modifiers": [
                                    [
                                        'darker',
                                        1.6
                                    ]
                                ]
                            },
                            axisTop=None,
                            axisRight=None,
                            axisBottom={
                                "tickSize": 5,
                                "tickPadding": 5,
                                "tickRotation": 0,
                                "legend": 'country',
                                "legendPosition": 'middle',
                                "legendOffset": 32,
                                "truncateTickAt": 0
                            },
                            axisLeft={
                                "tickSize": 5,
                                "tickPadding": 5,
                                "tickRotation": 0,
                                "legend": 'food',
                                "legendPosition": 'middle',
                                "legendOffset": -40,
                                "truncateTickAt": 0
                            },
                            labelSkipWidth=12,
                            labelSkipHeight=12,
                            labelTextColor={
                                "from": 'color',
                                "modifiers": [
                                    [
                                        'darker',
                                        1.6
                                    ]
                                ]
                            },
                            legends=[
                                {
                                    "dataFrom": 'keys',
                                    "anchor": 'bottom-right',
                                    "direction": 'column',
                                    "justify": False,
                                    "translateX": 120,
                                    "translateY": 0,
                                    "itemsSpacing": 2,
                                    "itemWidth": 100,
                                    "itemHeight": 20,
                                    "itemDirection": 'left-to-right',
                                    "itemOpacity": 0.85,
                                    "symbolSize": 20,
                                    "effects": [
                                        {
                                            "on": 'hover',
                                            "style": {
                                                "itemOpacity": 1
                                            }
                                        }
                                    ]
                                }
                            ],
                            role="application",
                            ariaLabel="Nivo bar chart demo",
                            # barAriaLabel=lambda
                            #     e: e.id + ": " + e.formattedValue + " in country: " + e.indexValue
                        )

                    )