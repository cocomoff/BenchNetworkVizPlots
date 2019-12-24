using Plots
using DelimitedFiles
gr()

function viz(nodes, edges; width=500, height=500, dpi=150)
    p = plot(size=(width, height), dpi=dpi, legend=false)

    # node X, Y
    nX = nodes[:, 2]
    nY = nodes[:, 3]
    plot!(p, nX, nY, seriestype=:scatter, color=:red, markershape=:circle, z=3)

    # edges (separate)
    for i in 1:size(edges)[1]
        u, v = edges[i, 1:2]
        u = Int(u) + 1
        v = Int(v) + 1
        pu, pv = nodes[u, 2:3], nodes[v, 2:3]
        plot!(p, [pu[1], pv[1]], [pu[2], pv[2]], linewidth=4, linecolor=:black, z=0)
    end
    p
end


function main()
    root = "python"
    basename = "tokyo_station"
    lD = collect(500:250:3000)

    for d in lD
        path_nodes = "$root/$(basename)_d$(d)_nodes.csv"
        path_edges = "$root/$(basename)_d$(d)_edges.csv"
        nodes = readdlm(path_nodes, ',')
        edges = readdlm(path_edges, ',')
        p = viz(nodes, edges)
        savefig(p, "$(basename)_$(d).png")
    end

end

main()