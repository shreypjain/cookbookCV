//
//  RecipeViewController.swift
//  cookbookCV
//
//  Created by Shrey Jain on 8/9/20.
//  Copyright © 2020 Shrey Jain. All rights reserved.
//

import UIKit

class RecipeViewController: UIViewController {
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let gradientLayer = CAGradientLayer()
        // Set the size of the layer to be equal to size of the display.
        gradientLayer.frame = view.bounds
        gradientLayer.startPoint = CGPoint(x: 0, y: 0.5) // Left side.
        gradientLayer.endPoint = CGPoint(x: 1, y: 0.5) // Right side.
        // Set an array of Core Graphics colors (.cgColor) to create the gradient.
        // This example uses a Color Literal and a UIColor from RGB values.
        gradientLayer.colors = [#colorLiteral(red: 0.1451525986, green: 0.2979582548, blue: 0.3310954571, alpha: 1).cgColor, #colorLiteral(red: 0.4389129281, green: 0.9021431804, blue: 0.7844631672, alpha: 1).cgColor]
        // Rasterize this static layer to improve app performance.
        gradientLayer.shouldRasterize = true
        // Apply the gradient to the backgroundGradientView.
        view.layer.addSublayer(gradientLayer)
        configureTableView()
        // Do any additional setup after loading the view.
    }
    
    func configureTableView() {
//        view.addSubview(tableView)
//        settableViewDelegates()
//        tableView.rowHeight = 100
//        tableView.backgroundColor = .systemTeal
//        //register cells
//        tableView.register(RecipeCell.self, forCellReuseIdentifier: "RecipeItem")
        //set constraints
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    func settableViewDelegates() {
//        tableView.delegate = self
//        tableView.dataSource = self
    }

}
//


